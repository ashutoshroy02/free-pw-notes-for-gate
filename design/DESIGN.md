# Design System: PW-Gate Pro

## Colors (OKLCH)
- `--bg-base`: `oklch(18% 0.01 250)` (Deep tinted dark)
- `--bg-surface`: `oklch(22% 0.01 250)` (Lighter surface)
- `--accent-primary`: `oklch(70% 0.15 250)` (Vibrant blue)
- `--accent-secondary`: `oklch(85% 0.15 80)` (Vibrant yellow/gold)
- `--text-primary`: `oklch(95% 0.01 250)`
- `--text-secondary`: `oklch(75% 0.01 250)`

## Typography
- **Headings**: "Outfit", sans-serif (Bold, 600+)
- **Body**: "Inter", sans-serif (400)
- **Monospace**: "JetBrains Mono"

## Elevation
- `--shadow-sm`: `0 2px 8px oklch(0% 0 0 / 20%)`
- `--shadow-md`: `0 8px 32px oklch(0% 0 0 / 40%)`

## Components
- **SubjectCard**: Interactive tile with hover-scale and entrance stagger.
- **GlassNavbar**: Sticky, minimal backdrop-blur.
- **QuickNav**: Bottom thumb-dock for mobile.

## Do's and Don'ts
- **Do**: Use generous whitespace (gap-8+).
- **Do**: Animate entrances with `cubic-bezier(0.16, 1, 0.3, 1)`.
- **Don't**: Use standard borders. Use background differentiation or shadows.
