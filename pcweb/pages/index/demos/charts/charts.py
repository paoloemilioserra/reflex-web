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
                        stop_color=rx.color("slate", 7), offset="5%", stop_opacity=0.8
                    ),
                    rx.el.svg.stop(
                        stop_color=rx.color("slate", 7), offset="95%", stop_opacity=0.1
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
                stroke=rx.color("violet", 8),
                fill="url(#gradientPurple)",
                # stack_id="1",
                type_="natural",
            ),
            rx.recharts.area(
                data_key="Desktop",
                stroke=rx.color("slate", 8),
                fill="url(#gradientSlate)",
                # stack_id="1",
                type_="natural",
            ),
            rx.recharts.graphing_tooltip(),
            # rx.recharts.cartesian_grid(),
            rx.recharts.x_axis(
                interval="preserveStartEnd",
                include_hidden=True,
                data_key="name",
                stroke="currentColor",
                type_="category",
                class_name="!font-small text-slate-9 [&>line]:!text-slateA-3",
            ),
            # rx.recharts.y_axis(),
            data=ChartsState.data,
            # stack_offset="none",
            width="100%",
            height="100%",
        ),
        class_name="flex flex-col items-end gap-6 p-8 h-full overflow-hidden",
    )
