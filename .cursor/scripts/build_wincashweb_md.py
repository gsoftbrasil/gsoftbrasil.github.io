#!/usr/bin/env python3
"""Gera version/WincashWeb.md a partir do histórico do ERP-GSOFT (develop + tags)."""
import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(r"C:\Users\Dev Manager\AppData\Local\Temp\erp-gsoft-tags")
OUT = Path(__file__).resolve().parents[2] / "version" / "WincashWeb.md"

EXCLUDE = re.compile(
    r"build/|Build Gsoft|Build Wincash Web|cursor/|doc/|docs/|"
    r"wincash-web-mobile|wincashwebmobile|wincashmobile|/mobile/|launcher|totem|pdvoff|pdv-off|"
    r"chore/|merge-|cardapiodigital|cardapio.?digital|"
    r"agent-spec|exemplo-casl|/skill|serializar.?json|remove.*\.env|vunerabilidade|"
    r"antigo frontend|postman|collections|feat/collection|rm/informacoes-sensiveis|"
    r"remove o webview|remove.*webview",
    re.I,
)
WEB = re.compile(r"wincash[- ]web|wincashweb", re.I)
API = re.compile(r"gsoftapi|gsoft-api", re.I)
DESKTOP = re.compile(r"wincash/", re.I)
PR_NUM = re.compile(r"\(#(\d+)\)")


def run(*args: str) -> str:
    r = subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        raise RuntimeError(r.stderr or r.stdout)
    return r.stdout


def branch_part(subject: str) -> str:
    return subject.split("(#")[0].strip() if "(#" in subject else subject


def classify(subject: str) -> str | None:
    if EXCLUDE.search(subject):
        return None
    branch = branch_part(subject)
    bl = branch.lower()
    if WEB.search(branch) and "mobile" not in bl:
        return "web"
    if API.search(branch):
        return "api"
    if DESKTOP.search(branch):
        return None
    return None


def br_date(iso_prefix: str) -> str:
    dt = datetime.strptime(iso_prefix[:10], "%Y-%m-%d")
    return dt.strftime("%d/%m/%Y")


def humanize(subject: str, body: str = "") -> str:
    s = PR_NUM.sub("", subject).strip()
    s = re.sub(r"^[\w.-]+/", "", s)
    parts = s.split("/")
    if len(parts) >= 2 and parts[0].lower() in ("feat", "fix", "refact", "refactor", "rm", "chore"):
        s = parts[-1]
    else:
        s = parts[-1] if parts else s
    s = s.replace("-", " ").replace("_", " ")

    known = {
        "multiemitente": "Suporte a **multi-emitente** no Wincash Web.",
        "rota fotos": "Nova rota de **fotos de produtos** na API.",
        "integraco whatsapp": "Integração com **WhatsApp** na Gsoft API.",
        "salvamento xml dfe": "Salvamento de **XML de DF-e** na Gsoft API.",
        "salvamento xml nfse": "Correção no salvamento de **XML de NFSe**.",
        "pedido compras filtrar produtos forncedor": "Filtro de produtos por **fornecedor** no pedido de compras.",
        "correcao websocket stop": "Melhorias de estabilidade no **WebSocket** (heartbeat, reconexão e watchdog).",
        "loader": "Indicador de **carregamento (loader)** nas telas do Wincash Web.",
        "salvardescartar": "Opções **salvar e descartar** em formulários do Wincash Web.",
        "rm projeto antigo": "Remoção do projeto legado da Gsoft API.",
        "cadastro cliente": "Tela de **cadastro de clientes** no Wincash Web.",
        "modulo de nota de entrada": "Módulo de **nota de entrada** no Wincash Web.",
        "movimentacao bancaria": "Tela de **movimentação bancária**.",
        "contas a receber": "Melhorias em **contas a receber**.",
        "doc estoque": "Documentação de estoque no Wincash Web.",
        "plano fechamento": "Plano de **fechamento de caixa** no Wincash Web.",
        "historico estoque v1": "**Histórico de estoque** no Wincash Web.",
        "consultar vendas": "Botão **consultar vendas** na aba Vendas.",
        "ticket/consultar vendas": "Botão **consultar vendas** na aba Vendas.",
    }
    key = s.lower().strip()
    if key in known:
        return known[key]

    text = ""
    for line in body.splitlines():
        t = line.strip().lstrip("*").strip()
        if not t or t.startswith("Merge ") or t.startswith("Build "):
            continue
        if t.startswith("Co-authored") or t.startswith("--------"):
            break
        if len(t) > 20:
            t = re.sub(r"^(feat|fix|refact):\s*", "", t, flags=re.I)
            if t[0].islower():
                t = t[0].upper() + t[1:]
            text = t
            break
    else:
        if s:
            label = s[0].upper() + s[1:]
            text = f"Melhorias em **{label}**."
        else:
            text = "Alteração no sistema."

    if not text:
        text = "Alteração no sistema."

    text = text.replace("\\", "/")
    if len(text) > 160:
        text = text[:157].rstrip() + "..."
    return text


def load_tags() -> list[tuple[str, str, str]]:
    raw = run(
        "for-each-ref",
        "--sort=creatordate",
        "--format=%(refname:short)|%(creatordate:iso8601)",
        "refs/tags",
    )
    tags = []
    for line in raw.strip().splitlines():
        if "|" not in line:
            continue
        name, iso = line.split("|", 1)
        tags.append((name, br_date(iso), iso[:10]))
    return tags


def release_date_for_commit(commit: str, tags: list[tuple[str, str, str]]) -> str:
    containing = run("tag", "--contains", commit, "--sort=creatordate").strip().splitlines()
    if containing:
        first = containing[0]
        for name, br, _ in tags:
            if name == first:
                return br
        iso = run("for-each-ref", f"refs/tags/{first}", "--format=%(creatordate:iso8601)").strip()
        if iso:
            return br_date(iso)
    iso = run("show", "-s", "--format=%ci", commit).strip()
    return br_date(iso)


def main():
    tags = load_tags()
    log = run("log", "develop", "--format=%H|%ci|%s")
    seen: set[int] = set()
    pr_info: dict[int, tuple[str, str, str]] = {}

    for line in log.strip().splitlines():
        if "|" not in line:
            continue
        commit, _ci, subject = line.split("|", 2)
        m = PR_NUM.search(subject)
        if not m:
            continue
        pr = int(m.group(1))
        if pr in seen:
            continue
        product = classify(subject)
        if not product:
            continue
        body = run("show", "-s", "--format=%b", commit)
        summary = humanize(subject, body)
        date = release_date_for_commit(commit, tags)
        pr_info[pr] = (product, date, summary)
        seen.add(pr)

    if 913 in pr_info and 912 in pr_info:
        del pr_info[912]

    by_date: dict[str, dict[str, list[tuple[int, str]]]] = defaultdict(
        lambda: {"web": [], "api": []}
    )
    for pr, (product, date, summary) in pr_info.items():
        by_date[date][product].append((pr, summary))

    sorted_dates = sorted(
        by_date.keys(),
        key=lambda d: datetime.strptime(d, "%d/%m/%Y"),
        reverse=True,
    )

    parts = [
        "# Wincash Web",
        "",
        "Esta página reúne as alterações do **Wincash Web** e da **Gsoft API** (serviço local de integração).",
        "A atualização é automática — não há download manual.",
        "",
    ]

    for date_str in sorted_dates:
        block = by_date[date_str]
        if not block["web"] and not block["api"]:
            continue
        parts.append(f"### {date_str}")
        if block["web"]:
            parts.append("**Wincash Web**")
            for pr_num, summary in sorted(block["web"], key=lambda x: -x[0]):
                parts.append(f"* ``PR {pr_num}``: {summary}")
            parts.append("")
        if block["api"]:
            parts.append("**Gsoft API**")
            for pr_num, summary in sorted(block["api"], key=lambda x: -x[0]):
                parts.append(f"* ``PR {pr_num}``: {summary}")
            parts.append("")

    OUT.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    web_count = sum(len(by_date[d]["web"]) for d in by_date)
    api_count = sum(len(by_date[d]["api"]) for d in by_date)
    print(f"Written {OUT}")
    print(f"Dates: {len(sorted_dates)}, Web PRs: {web_count}, API PRs: {api_count}")


if __name__ == "__main__":
    main()
