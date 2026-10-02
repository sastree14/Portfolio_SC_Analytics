from __future__ import annotations

from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "visual-previews"

PROJECTS = [
    ("SC-01", "Long-Running AI Agent Platform", "sc-01-long-running-agent-platform"),
    ("SC-02", "Multi-Agent Operations Orchestrator", "sc-02-multi-agent-operations-orchestrator"),
    ("SC-03", "AI Sales & CRM Automation System", "sc-03-ai-sales-crm-automation"),
    ("SC-04", "AI Receptionist & Lead Qualification", "sc-04-ai-receptionist-lead-qualification"),
    ("SC-05", "Document Intelligence & Due Diligence Agent", "sc-05-document-intelligence-due-diligence-agent"),
    ("SC-06", "AI Workflow Automation Hub", "sc-06-ai-workflow-automation-hub"),
    ("SC-07", "Full-Stack LLM Business Copilot", "sc-07-full-stack-llm-business-copilot"),
    ("SC-08", "Enterprise Data Integration & API Platform", "sc-08-enterprise-data-integration-api-platform"),
    ("SC-09", "ETL / ELT & Data Quality Pipeline", "sc-09-etl-elt-data-quality-pipeline"),
    ("SC-10", "Real-Time Analytics & Monitoring Platform", "sc-10-real-time-analytics-platform"),
    ("SC-11", "ML / AI Evaluation & Monitoring Platform", "sc-11-mlops-evaluation-monitoring"),
    ("SC-12", "Multi-Horizon Demand Forecasting & Inventory Planning", "sc-12-multi-horizon-demand-forecasting"),
    ("SC-13", "R Shiny Forecasting & Scenario Planning Application", "sc-13-r-shiny-forecasting-scenario-planning"),
    ("SC-14", "Power BI Executive Decision System", "sc-14-power-bi-executive-decision-system"),
    ("SC-15", "Tableau Commercial Analytics & Drill-Down", "sc-15-tableau-commercial-analytics"),
    ("SC-16", "Recommendation, Search & Ranking Engine", "sc-16-recommendation-search-ranking-engine"),
    ("SC-17", "Customer Intelligence: Churn, CLV & Segmentation", "sc-17-customer-intelligence-churn-clv"),
    ("SC-18", "Credit Risk & Profit Optimization Engine", "sc-18-credit-risk-profit-optimization"),
    ("SC-19", "Fraud Detection & Explainability System", "sc-19-fraud-detection-explainability"),
    ("SC-20", "Supply Chain & Marketplace Optimization", "sc-20-supply-chain-optimization"),
    ("SC-21", "Pricing & Revenue Optimization Engine", "sc-21-pricing-revenue-optimization"),
    ("SC-22", "Resource, Capacity & Scheduling Optimization", "sc-22-resource-capacity-scheduling-optimization"),
    ("SC-23", "Operations Simulation & What-If Engine", "sc-23-operations-simulation-what-if"),
    ("SC-24", "Financial Modelling & Scenario Engine", "sc-24-financial-modelling-scenario-engine"),
    ("SC-25", "Debt, Cash Flow & Investment Model", "sc-25-debt-cashflow-investment-model"),
    ("SC-26", "Portfolio Risk & Capital Allocation Engine", "sc-26-portfolio-risk-capital-allocation"),
    ("SC-27", "Quantitative Trading & Market Microstructure System", "sc-27-quant-trading-market-microstructure"),
    ("SC-28", "AI Property Development Feasibility & Operations System", "sc-28-ai-property-development-feasibility"),
    ("SC-29", "Commercial Due Diligence & Market Intelligence System", "sc-29-commercial-due-diligence-market-intelligence"),
    ("SC-30", "Computer Vision Waste Detection & Sorting System", "sc-30-computer-vision-waste-detection-sorting"),
    ("SC-31", "Power BI Forecast & Inventory Planning Dashboard", "sc-31-power-bi-forecast-inventory-planning"),
    ("SC-32", "Power BI Order Fulfilment & Service Control Tower", "sc-32-power-bi-order-fulfilment-control-tower"),
]


def font(size: int):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def render_all() -> list[tuple[str, str, Path]]:
    OUT.mkdir(exist_ok=True)
    rendered = []
    for project_id, title, slug in PROJECTS:
        src = ROOT / "projects" / slug / "examples" / "visuals" / "result.svg"
        dst = OUT / f"{project_id.lower()}-{slug[6:]}.png"
        cairosvg.svg2png(url=str(src), write_to=str(dst), output_width=1200, output_height=720)
        rendered.append((project_id, title, dst))
    return rendered


def contact_sheet(items: list[tuple[str, str, Path]], name: str) -> None:
    cols = 3
    tile_w, tile_h = 400, 285
    image_w, image_h = 370, 222
    header_h = 64
    rows = (len(items) + cols - 1) // cols

    canvas = Image.new("RGB", (cols * tile_w, header_h + rows * tile_h), "white")
    draw = ImageDraw.Draw(canvas)
    draw.text((24, 18), name, fill=(15, 23, 42), font=font(24))

    for idx, (project_id, title, path) in enumerate(items):
        row, col = divmod(idx, cols)
        x = col * tile_w + 15
        y = header_h + row * tile_h + 12

        img = Image.open(path).convert("RGB")
        img.thumbnail((image_w, image_h), Image.Resampling.LANCZOS)
        canvas.paste(img, (x, y))

        draw.text((x, y + 228), f"{project_id} · {title}", fill=(15, 23, 42), font=font(13))
        draw.line((x, y + 254, x + image_w, y + 254), fill=(226, 232, 240), width=1)

    canvas.save(OUT / f"{name.lower().replace(' ', '-')}.png", optimize=True)


def main() -> None:
    rendered = render_all()
    contact_sheet(rendered[:10], "SC-Analytics Visuals 01-10")
    contact_sheet(rendered[10:20], "SC-Analytics Visuals 11-20")
    contact_sheet(rendered[20:], "SC-Analytics Visuals 21-32")
    print(f"Rendered {len(rendered)} visual PNGs and 3 contact sheets.")


if __name__ == "__main__":
    main()
