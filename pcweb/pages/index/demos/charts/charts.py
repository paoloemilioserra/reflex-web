import reflex as rx
from pcweb.components.button import button
import random

data = [
    {
        "name": "Jan",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
    {
        "name": "Feb",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
    {
        "name": "Mar",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
    {
        "name": "Apr",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
    {
        "name": "May",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
    {
        "name": "Jun",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
    {
        "name": "Jul",
        "Mobile": random.randint(100, 500),
        "Desktop": random.randint(400, 800),
    },
]


class ChartsState(rx.State):
    data = data

    def randomize_data(self):
        self.data = [
            {
                "name": item["name"],
                "Mobile": random.randint(100, 500),
                "Desktop": random.randint(400, 800),
            }
            for item in self.data
        ]


def charts():
    return rx.box(
        rx.el.style(
            """
.recharts-tooltip-item-unit {
    display: none;
}
.recharts-tooltip-item-value {
    font-family: "JetBrains Mono", monospace;
    color: var(--c-slate-12);
}

.recharts-tooltip-item:first-child .recharts-tooltip-item-name {
    color: var(--c-violet-9);
}

.recharts-tooltip-item:nth-child(2) .recharts-tooltip-item-name {
    color: var(--c-slate-10);
}
.recharts-tooltip-item-list {
    margin-top: 4px !important;
}
"""
        ),
        button("Randomize", variant="secondary", on_click=ChartsState.randomize_data),
        rx.recharts.area_chart(
            rx.el.svg.defs(
                rx.el.svg.linear_gradient(
                    rx.el.svg.stop(
                        stop_color=rx.color("violet", 7), offset="5%", stop_opacity=0.8
                    ),
                    rx.el.svg.stop(
                        stop_color=rx.color("violet", 7), offset="95%", stop_opacity=0.1
                    ),
                    x1=0,
                    x2=0,
                    y1=0,
                    y2=1,
                    id="gradientPurple",
                ),
            ),
            rx.el.svg.defs(
                rx.el.svg.linear_gradient(
                    rx.el.svg.stop(
                        stop_color="var(--c-slate-7)", offset="5%", stop_opacity=0.8
                    ),
                    rx.el.svg.stop(
                        stop_color="var(--c-slate-7)", offset="95%", stop_opacity=0.1
                    ),
                    x1=0,
                    x2=0,
                    y1=0,
                    y2=1,
                    id="gradientSlate",
                ),
            ),
            rx.recharts.area(
                data_key="Mobile",
                stroke="var(--c-violet-8)",
                fill="url(#gradientPurple)",
                type_="natural",
                active_dot={
                    "stroke": "var(--c-violet-9)",
                    "fill": "var(--c-violet-9)",
                },
            ),
            rx.recharts.area(
                data_key="Desktop",
                stroke="var(--c-slate-8)",
                fill="url(#gradientSlate)",
                type_="natural",
                active_dot={
                    "stroke": "var(--c-slate-10)",
                    "fill": "var(--c-slate-10)",
                },
            ),
            rx.recharts.graphing_tooltip(
                content_style={
                    "background": "var(--c-slate-1)",
                    "borderColor": "var(--c-slate-5)",
                    "borderRadius": "0.75rem",
                    "boxShadow": "0px 2px 4px 0px rgba(28, 32, 36, 0.05)",
                    "fontFamily": "var(--font-instrument-sans)",
                    "fontFamily": "var(--font-instrument-sans)",
                    "fontSize": "0.9rem",
                    "fontStyle": "normal",
                    "fontWeight": "500",
                    "lineHeight": "1rem",
                    "letterSpacing": "-0.01094rem",
                    "minWidth": "8rem",
                    "padding": "6px 10px",
                    "position": "relative",
                    "::after": {
                        "content": "''",
                        "position": "absolute",
                        "left": "0",
                        "top": "0",
                        "width": "4px",
                        "height": "100%",
                        "backgroundColor": "var(--c-violet-9)",
                        "borderTopLeftRadius": "0.75rem",
                        "borderBottomLeftRadius": "0.75rem",
                    },
                },
                item_style={
                    "color": "currentColor",
                    "display": "flex",
                    "paddingBottom": "0px",
                    "justifyContent": "space-between",
                },
                label_style={"color": "var(--c-slate-12)"},
                cursor={
                    "strokeWidth": 1,
                    "stroke": "var(--slate-a5)",
                    "fill": "var(--slate-a5)",
                },
                separator="",
            ),
            rx.recharts.cartesian_grid(
                horizontal=True, vertical=False, class_name="!stroke-slateA-3"
            ),
            rx.recharts.x_axis(
                # interval="preserveStartEnd",  # This prop doesn't exist in the current reflex version
                include_hidden=True,
                data_key="name",
                stroke="currentColor",
                type_="category",
                class_name="!font-small text-slate-9 [&>line]:!text-slateA-3",
            ),
            data=ChartsState.data,
            class_name="w-full h-full overflow-visible",
        ),
        class_name="flex flex-col items-end gap-6 p-8 h-full overflow-hidden",
    )
