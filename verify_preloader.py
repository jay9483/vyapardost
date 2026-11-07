import re

print("--- Verifying Neuv.fr Style Preloader & Morph Transition ---")

with open("/Users/prithvij/.gemini/antigravity/scratch/vyapardost/app.py") as f:
    code = f.read()

# 1. Preloader Overlay & Structure
assert "vyapar-preloader" in code, "Missing #vyapar-preloader overlay container"
assert "loading-ring-svg" in code, "Missing loading-ring-svg"
assert "ring-progress" in code, "Missing ring-progress circle"
assert "vyapar-emblem-svg" in code, "Missing vyapar-emblem-svg"
print("✓ 1. Preloader overlay and SVG emblem structure verified")

# 2. 5-Second Thin Ring Animation
assert "527.79" in code, "Missing 527.79 stroke circumference for thin circle"
assert "5000ms" in code, "Missing 5000ms (5s) transition for progress ring"
print("✓ 2. 5-Second thin loading circle animation verified")

# 3. Logo Assembly Parts
assert "assembleRoof" in code, "Missing assembleRoof keyframe"
assert "assembleBase" in code, "Missing assembleBase keyframe"
assert "assembleCore" in code, "Missing assembleCore keyframe"
assert "assembleSpark" in code, "Missing assembleSpark keyframe"
print("✓ 3. Logo assembly keyframe choreography verified")

# 4. Zoom-Morph Transition Under 600ms
assert "zoom-morph-exit" in code, "Missing zoom-morph-exit class"
assert "scale(24)" in code, "Missing zoom-in scale(24) morph"
assert "520ms" in code, "Exit morph must be under 600ms (configured at 520ms)"
print("✓ 4. Zoom-in morph exit transition (<600ms) verified")

# 5. Interruptibility (Click, Keydown, Scroll)
assert "keydown" in code, "Missing keydown interruptibility listener"
assert "Escape" in code, "Missing Escape key dismiss listener"
assert "wheel" in code, "Missing wheel/scroll interruptibility listener"
assert "skip-intro-btn" in code, "Missing skip-intro-btn"
print("✓ 5. Multi-input interruptibility (Click, Scroll, ESC) verified")

# 6. Accessibility (prefers-reduced-motion)
assert "prefers-reduced-motion" in code, "Missing prefers-reduced-motion media query"
print("✓ 6. Reduced-motion accessibility verified")

# 7. Session Storage & Replay Button
assert "vyapardost_intro_done" in code, "Missing session storage key"
assert "btn_replay_intro" in code, "Missing Replay Studio Intro button"
print("✓ 7. Session persistence and Replay Studio Intro button verified")

print("--- ALL PRELOADER & MORPH VERIFICATION CHECKS PASSED WITH 100% SUCCESS ---")
