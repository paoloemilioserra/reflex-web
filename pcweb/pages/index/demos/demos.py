import reflex as rx

from .auth.auth import auth
from .forms.forms import forms
from .dashboard.dashboard import dashboard
from .image_gen.image_gen import image_gen, image_gen_code, image_gen_2
from .charts.charts import charts
from reflex_type_animation import type_animation


class DemoState(rx.State):

    demo = "Image Gen"

    def set_demo(self, demo):
        self.demo = demo


# def example_button(text):
#     return rx.button(
#     text,
#     border_radius="8px;",
#     border="1px solid var(--c-slate-5);",
#     color=rx.cond(
#         DemoState.demo == text,
#         "white",
#         "var(--c-slate-9)",
#     ),
#     background= rx.cond(
#         DemoState.demo == text,
#         "var(--c-violet-9)",
#         "var(--c-slate-2)",
#     ),
#     backdrop_filter= "blur(2px);",
#     on_click= lambda: DemoState.set_demo(text)
# )

# def heading():
#     return rx.vstack(
#         type_animation(
#             sequence=[
#                 "Build web apps, faster.",
#                 1000,
#                 "Build internal tools, faster.",
#                 1000,
#                 "Build AI apps, faster.",
#                 1000,
#                 "Build web apps, faster.",
#             ],
#             font_size=["24px", "30px", "44px", "44px", "44px", "44px"],
#             text_align="left",
#             color="var(--c-slate-11)",
#             font_weight="bold",
#             line_height="1",
#         ),
#         rx.el.h3(
#             "Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend.",
#             color="var(--c-slate-10)",
#             font_size=[".8em", ".8em", "1em", "1em", "1em", "1em"],
#             text_align="center",
#             class_name="font-small"
#         ),
#         padding_y="1em",
#     )

# def more_examples():
#     return rx.link(
#                 rx.button(
#                     "More Examples",
#                     rx.icon(
#                         "chevron-right",
#                         size=18,
#                         stroke_width="1px",
#                         padding_left=".1em",
#                     ),
#                     background="var(--c-slate-2)",
#                     color="var(--c-slate-9)",
#                     border_radius="8px;",
#                     border="1px solid var(--c-slate-5);",
#                     text_wrap="nowrap",
#                 ),
#                 href="/gallery",
#             )

# def demos():
#     return rx.flex(
#         heading(),
#         rx.hstack(
#             rx.hstack(
#                 example_button("Image Gen"),
#                 example_button("Forms"),
#                 example_button("Auth"),
#                 example_button("Dashboard"),
#                 max_width="35em",
#                 overflow_x="scroll",
#                 scrollbar_width= "none"
#             ),
#             rx.spacer(),
#             more_examples(),
#             align_items="left",
#             width="100%",
#         ),
#         rx.box(
#             rx.match(
#                 DemoState.demo,
#                 ("Forms", forms()),
#                 ("Dashboard", dashboard()),
#                 ("Auth", auth()),
#                 ("Image Generator", image_gen()),
#                 image_gen()
#             ),
#             border_radius= "10px;",
#             border= "1px solid var(--c-slate-5);",
#             background_color= "var(--c-slate-2)",
#             overflow="hidden",
#             width="100%",
#         ),
#         padding_bottom="4em",
#         width="100%",
#         direction="column",
#         # background_image="url(/grid.png)",
#         background_position= ["50% 50%;", "50% 40%;", "50% 70%;", "50% 70%;", "50% 70%;", "50% 70%;"],
#         background_repeat= "no-repeat;",
#         background_size= "auto;",
#         padding_top="5em",
#         gap="1em",
#         class_name="bg-slate-1"
#     )


def tab(name: str, icon: str) -> rx.Component:
    is_selected = DemoState.demo == name
    return rx.box(
        rx.icon(tag=icon, size=16),
        name,
        class_name="flex flex-row justify-center items-center gap-2 hover:bg-slate-3 px-3 py-[0.125rem] rounded-[0.625rem] h-8 font-small text-slate-9 transition-bg cursor-pointer box-border"
        + rx.cond(is_selected, " border border-slate-5 bg-slate-1", ""),
        on_click=DemoState.set_demo(name),
    )


def code_block(code: str) -> rx.Component:
    return rx.code_block(
        code,
        language="python",
        # wrap_long_lines=True,
        class_name="demo-code-block border-slate-4 !p-8 border-r !rounded-none",
    )


def preview_block() -> rx.Component:
    return rx.box(
        rx.text("Preview"),
        class_name="flex justify-center items-center p-8 w-full h-full",
    )


text_code = """def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def event_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="calendar-plus", size=32),
                    color_scheme="mint",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Create an event",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Fill the form to create a custom event",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    form_field(
                        "Event Name",
                        "Event Name",
                        "text",
                        "event_name",
                    ),
                    rx.flex(
                        form_field(
                            "Date", "", "date", "event_date"
                        ),
                        form_field(
                            "Time", "", "time", "event_time"
                        ),
                        spacing="3",
                        flex_direction="row",
                    ),
                    form_field(
                        "Description",
                        "Optional",
                        "text",
                        "description",
                    ),
                    direction="column",
                    spacing="2",
                ),
                rx.form.submit(
                    rx.button("Create"),
                    as_child=True,
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string()
                ),
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )
"""


def demo_section() -> rx.Component:
    return rx.box(
        # Tabs
        rx.box(
            tab("Image Gen", "wand-sparkles"),
            tab("Forms", "scan-text"),
            tab("Charts", "layout-panel-left"),
            tab("Authorization", "folder-open-dot"),
            tab("More", "layers"),
            class_name="flex flex-row items-center gap-2 border-slate-4 p-2 border-b",
        ),
        # Preview
        # TODO: Add the real previews
        rx.box(
            rx.box(
                rx.match(
                    DemoState.demo,
                    ("Image Gen", code_block(image_gen_code)),
                    ("Forms", code_block(image_gen_code)),
                    ("Charts", code_block(image_gen_code)),
                    ("Authorization", code_block(image_gen_code)),
                    # ("More", more()),
                    image_gen(),
                ),
                class_name="w-1/2 overflow-auto",
            ),
            rx.box(
                rx.match(
                    DemoState.demo,
                    ("Image Gen", image_gen_2()),
                    ("Forms", image_gen()),
                    ("Charts", charts()),
                    ("Authorization", auth()),
                    # ("More", more()),
                    image_gen(),
                ),
                class_name="w-1/2 h-auto",
            ),
            class_name="flex flex-row w-full h-full max-h-[34rem] overflow-hidden",
        ),
        class_name="flex flex-col border-slate-4 bg-slate-2 shadow-large border rounded-[1.125rem] w-full max-w-[67rem] h-full overflow-hidden",
    )
