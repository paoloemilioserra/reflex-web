import reflex as rx
from pcweb.pages.docs import getting_started
from pcweb.components.button import button
from pcweb.components.icons.icons import get_icon

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


def tab(name: str, icon: str, is_selected: bool) -> rx.Component:
    return rx.box(
        rx.icon(tag=icon, size=16),
        name,
        class_name="flex flex-row justify-center items-center gap-2 hover:bg-slate-3 px-3 py-[0.125rem] rounded-[0.625rem] h-8 font-small text-slate-9 transition-bg cursor-pointer"
        + (" border border-slate-5 bg-slate-1" if is_selected else ""),
    )


def code_block(code: str) -> rx.Component:
    return rx.code_block(
        code,
        language="python",
        # wrap_long_lines=True,
        class_name="demo-code-block border-slate-4 !p-8 border-r",
    )


def preview_block() -> rx.Component:
    return rx.box(
        rx.text("Preview"),
        class_name="flex justify-center items-center p-8 w-full h-full",
    )


def demo_section() -> rx.Component:
    return rx.box(
        # Tabs
        rx.box(
            tab("Image Gen", "wand-sparkles", True),
            tab("Forms", "scan-text", False),
            tab("Dashboard", "layout-panel-left", False),
            tab("Authorization", "folder-open-dot", False),
            tab("More", "layers", False),
            class_name="flex flex-row items-center gap-2 border-slate-4 p-2 border-b",
        ),
        # Preview
        # TODO: Add the real previews
        rx.box(
            code_block(text_code),
            preview_block(),
            class_name="grid grid-cols-2 w-full h-full overflow-hidden",
        ),
        class_name="flex flex-col border-slate-4 bg-slate-2 shadow-large border rounded-[1.125rem] w-full max-w-[67rem] h-full max-h-[35rem] overflow-hidden",
    )


def hero() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.el.section(
        # Headings
        rx.box(
            rx.el.h1(
                "Build web apps in pure Python",
                class_name="inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full font-xxx-large text-balance text-center text-transparent",
            ),
            rx.el.h2(
                rx.el.span("An open-source framework to ship beautiful apps fast."),
                rx.el.span("Deploy with a single command."),
                class_name="flex flex-col font-md text-center text-slate-9",
            ),
            class_name="flex flex-col gap-6",
        ),
        # Buttons
        rx.box(
            rx.link(
                button(
                    "Get Started",
                    class_name="!px-5 !py-2 !h-12 !font-smbold !text-[1.125rem] !leading-[1.625rem] !tracking-[-0.01688rem]",
                ),
                underline="none",
                href=getting_started.introduction.path,
            ),
            rx.link(
                button(
                    "Get a demo",
                    variant="secondary",
                    class_name="!px-5 !py-2 !h-12 !font-semibold !text-[1.125rem] !leading-[1.625rem] !tracking-[-0.01688rem] transition-bg",
                ),
                href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX",
                is_external=True,
                underline="none",
            ),
            class_name="flex flex-row items-center gap-4",
        ),
        # Pip install
        rx.box(
            get_icon("copy", class_name="!text-slate-9 [&>svg]:w-4 [&>svg]:h-4"),
            rx.el.p(
                "$ pip install reflex",
                class_name="font-['JetBrains_Mono'] font-medium font-small text-[0.8125rem] text-center text-slate-9 leading-6",
            ),
            class_name="flex flex-row items-center gap-3 hover:bg-slate-3 px-3 py-2 rounded-xl cursor-pointer transition-bg",
        ),
        # Demo section
        demo_section(),
        class_name="flex flex-col justify-center items-center gap-8 mx-auto px-4 md:px-6 w-full max-w-6xl",
    )
