from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "media"
OUT = MEDIA / "cupsafe-slack-desk-demo.mp4"
W, H = 1920, 1080
FPS = 24


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = font(76, True)
F_H1 = font(54, True)
F_H2 = font(38, True)
F_BODY = font(30)
F_SMALL = font(24)
F_MONO = font(26)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def rounded(draw, box, fill, outline=None, width=2, radius=22):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def base():
    img = Image.new("RGB", (W, H), "#f5f7fb")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, W, 130), fill="#3f0e40")
    draw.text((80, 42), "CupSafe Slack Desk", font=F_H2, fill="#ffffff")
    draw.text((1470, 48), "Slack Agent Demo", font=F_SMALL, fill="#d9c7e8")
    return img, draw


def text_block(draw, x, y, text, fnt=F_BODY, fill="#263244", width=740, line_h=42):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += line_h
    return y


def draw_decision_card(draw, x, y, title, decision, severity, body, color):
    rounded(draw, (x, y, x + 760, y + 155), "#ffffff", "#d5dce8")
    draw.text((x + 28, y + 24), title, font=F_H2, fill="#172033")
    draw.rounded_rectangle((x + 560, y + 24, x + 718, y + 72), radius=16, fill=color)
    draw.text((x + 585, y + 34), decision, font=F_SMALL, fill="#ffffff")
    draw.text((x + 28, y + 79), f"Severity: {severity}", font=F_SMALL, fill="#57657a")
    text_block(draw, x + 28, y + 112, body, F_SMALL, "#334155", 690, 30)


def scene_title(progress):
    img, draw = base()
    draw.text((110, 245), "Wallet-risk triage inside Slack", font=F_TITLE, fill="#172033")
    text_block(
        draw,
        115,
        365,
        "A support-safe agent concept that turns wallet incident reports into ALLOW, REVIEW, or DENY decisions before a user signs.",
        F_BODY,
        "#4d5a70",
        1040,
        44,
    )
    rounded(draw, (115, 585, 845, 775), "#ffffff", "#d5dce8")
    text_block(draw, 155, 630, "No private keys. No wallet connection. No customer data.", F_H2, "#172033", 650, 52)
    draw_progress(draw, progress)
    return img


def scene_problem(progress):
    img, draw = base()
    draw.text((95, 205), "The problem", font=F_TITLE, fill="#172033")
    bullets = [
        "Users ask support for help while a risky approval is already open.",
        "Support teams need evidence fast, without asking for private keys.",
        "Prior scam memory should guide the next transaction decision.",
    ]
    y = 335
    for item in bullets:
        draw.ellipse((110, y + 11, 130, y + 31), fill="#36c5f0")
        y = text_block(draw, 155, y, item, F_BODY, "#263244", 1120, 44) + 22
    rounded(draw, (1180, 260, 1760, 640), "#ffffff", "#d5dce8")
    draw.text((1225, 305), "Input", font=F_H2, fill="#172033")
    text_block(draw, 1225, 375, "Slack incident text, counterparty, amount, approval scope, and risk tags.", F_BODY, "#4d5a70", 460, 42)
    draw_progress(draw, progress)
    return img


def scene_demo(progress):
    img, draw = base()
    draw.text((95, 175), "Local demo decisions", font=F_TITLE, fill="#172033")
    draw_decision_card(
        draw,
        110,
        300,
        "Support DM asks for unlimited approval",
        "DENY",
        "critical",
        "Blocks unverified approval and recommends revoking allowance.",
        "#c92f54",
    )
    draw_decision_card(
        draw,
        1020,
        300,
        "Verified merchant checkout",
        "ALLOW",
        "low",
        "Allows bounded payment backed by prior merchant memory.",
        "#2e8b57",
    )
    draw_decision_card(
        draw,
        110,
        520,
        "Bridge route with fresh contract",
        "REVIEW",
        "elevated",
        "Escalates slippage and fresh-contract signals to humans.",
        "#b7791f",
    )
    draw_decision_card(
        draw,
        1020,
        520,
        "High slippage DEX route",
        "REVIEW",
        "elevated",
        "Drafts a safe reply and routes to security triage.",
        "#b7791f",
    )
    draw.text((110, 785), "Verification: scripts/verify-slack-demo.mjs passes 4/4 cases.", font=F_BODY, fill="#263244")
    draw_progress(draw, progress)
    return img


def scene_arch(progress):
    img, draw = base()
    draw.text((95, 175), "Target architecture", font=F_TITLE, fill="#172033")
    arch_path = MEDIA / "slack-cupsafe-architecture.png"
    if arch_path.exists():
        arch = Image.open(arch_path).convert("RGB")
        arch.thumbnail((1180, 720))
        img.paste(arch, (95, 285))
    rounded(draw, (1340, 310, 1780, 675), "#ffffff", "#d5dce8")
    text_block(draw, 1375, 350, "Slack command + message action -> hosted agent endpoint -> risk memory -> support-safe reply.", F_BODY, "#263244", 360, 42)
    draw_progress(draw, progress)
    return img


def scene_links(progress):
    img, draw = base()
    draw.text((95, 190), "Current submission assets", font=F_TITLE, fill="#172033")
    items = [
        ("Hosted demo", "https://bingfasamsung-boop.github.io/cupsafe-slack-desk/"),
        ("Source code", "https://github.com/bingfasamsung-boop/cupsafe-slack-desk"),
        ("Slack sandbox", "CupSafe Slack Desk workspace and app created"),
        ("Honest status", "Static demo is live; slash-command backend still needs a real POST endpoint"),
    ]
    y = 330
    for label, value in items:
        rounded(draw, (115, y, 1730, y + 115), "#ffffff", "#d5dce8")
        draw.text((155, y + 24), label, font=F_H2, fill="#172033")
        draw.text((500, y + 34), value, font=F_MONO, fill="#3867d6")
        y += 145
    draw_progress(draw, progress)
    return img


def draw_progress(draw, progress):
    draw.rounded_rectangle((80, 1010, 1840, 1030), radius=10, fill="#d9e0ec")
    draw.rounded_rectangle((80, 1010, 80 + int(1760 * progress), 1030), radius=10, fill="#36c5f0")


SCENES = [scene_title, scene_problem, scene_demo, scene_arch, scene_links]


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    total_frames = 60 * FPS
    scene_frames = total_frames // len(SCENES)
    with imageio.get_writer(OUT, fps=FPS, codec="libx264", quality=8, macro_block_size=16) as writer:
        for i in range(total_frames):
            scene_idx = min(i // scene_frames, len(SCENES) - 1)
            progress = (i + 1) / total_frames
            frame = SCENES[scene_idx](progress)
            writer.append_data(np.asarray(frame))
    print(OUT)


if __name__ == "__main__":
    main()
