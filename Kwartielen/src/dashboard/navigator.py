class DashboardNavigator:
    """Handle left/right keyboard navigation across dashboard pages."""

    def __init__(self, stats, brand_names, pages):
        self._stats = stats
        self._brand_names = brand_names
        self._pages = pages
        self._current_page = 0

    def render_current_page(self, figure, axis) -> None:
        """Render the active page into the provided matplotlib axis."""
        title, renderer = self._pages[self._current_page]
        renderer(self._stats, self._brand_names, axis)
        figure.suptitle(
            f"Battery Dashboard: {title} ({self._current_page + 1}/{len(self._pages)})",
            fontsize=15,
            fontweight="bold",
        )
        axis.text(
            0.5,
            -0.14,
            "Use left/right arrow keys to switch views",
            transform=axis.transAxes,
            ha="center",
            fontsize=10,
        )
        figure.tight_layout()

    def handle_key_press(self, event, figure, axis) -> None:
        """Move backward or forward through dashboard pages."""
        if event.key not in ("left", "right"):
            return

        if event.key == "right":
            self._current_page = (self._current_page + 1) % len(self._pages)
        else:
            self._current_page = (self._current_page - 1) % len(self._pages)

        self.render_current_page(figure, axis)
        figure.canvas.draw_idle()
