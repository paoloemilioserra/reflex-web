import reflex as rx
from .logo import landing
from pcweb.pages.docs import getting_started

def feature_button(name: str):
    return rx.box(
        name,
        class_name="border-slate-5 bg-slate-2 px-3 py-1 border rounded-full font-small text-slate-9 shadow-small",
    )

def feature_button_hstack(mobile=False):
    return rx.hstack(
        feature_button("Frontend"),
        feature_button("Backend"),
        feature_button("Hosting"),
        justify="start" if not mobile else "center",
        width="100%",
    )


def hero_section_text(mobile=False):
    return rx.vstack(
        rx.el.h1(
            "Web apps in pure Python.",
            text_align="left" if not mobile else "center",
            font_size=["24px", "30px", "40px", "54px", "54px", "54px"],
            font_weight="bold",
            line_height="1",
            class_name="inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full text-start text-transparent",
        ),
        rx.el.h2(
            "Deploy with a single command.",
            text_align="left" if not mobile else "center",
            color="var(--c-slate-11)",
            font_size=["24px", "30px", "40px", "54px", "54px", "54px"],
            font_weight="bold",
            line_height="1",
            max_width=["200px", "300px", "400px", "650px", "650px", "650px"],
        ),
        align_items="center" if mobile else "start",
    )

def hero_section_buttons(mobile=False):
    button_size={
        "padding_y": "1.5em",
        "padding_x": "2em",
        "border_radius": "8px",
        "color":"#FFFFFF",
        "align_items":"center",
        "justify_content":"center",
        "font_weight":"400",
        "font_size":"1em",
    }
    return rx.hstack(
        rx.link(
            rx.flex(
                rx.button(
                    "Get Started",
                    rx.icon(
                    tag="chevron-right",
                        size=18,
                        stroke_width="1px",
                        padding_left=".1em",
                    ),
                    background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%)",
                    box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset",
                    display= "inline-flex;",   
                    border= "1px solid transparent;", 
                    style=button_size,
                ),
                _hover={
                    "border": "1px solid rgba(94, 78, 242, .15)",
                },
                border= "1px solid transparent;",
                padding="3px",
                border_radius="8px",
            ),
            cursor="pointer",
            underline="none",
            href=getting_started.introduction.path,        
        ),
        rx.link(
            rx.button(
                "Get a demo ",
                rx.icon(
                    tag="chevron-right",
                    size=18,
                    stroke_width="1px",
                    padding_left=".1em",
                ),
                bg="none",
                _hover={
                    "background": "linear-gradient(115deg, #1D1B23 14.13%, #131217 73.41%)",
                    "color": "white",
                    "box-shadow": "0px 0px 27px -4px rgba(0, 0, 0, 0.30), 0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset;"
                },
                color=rx.color_mode_cond("black", "white"),
                style=button_size,
            ),
            href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX", 
            is_external=True,
            margin_left=".25em",   
            cursor="pointer", 
            underline="none",    
        ),
        align_items="center",
        justify="start" if not mobile else "center",
        width="100%",
    )

def hero_section() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.center(
        rx.chakra.vstack(
            landing(),
            rx.desktop_only(rx.vstack(
                feature_button_hstack(),
                hero_section_text(),
                hero_section_buttons(),
                padding_left="3em",
                spacing="5",
                align_items="left",
            )),
            rx.mobile_and_tablet(
                rx.vstack(
                    #feature_button_hstack(mobile=True),
                    hero_section_text(mobile=True),
                    hero_section_buttons(mobile=True),
                    spacing="5",
                    margin_top=["-4em", "-3em", "-1em", "0", "0", "0"],
                ),
            ),
            direction="column",
            align_items="left",
            margin_top=["-6em", "-4em", "0", "0", "0", "0"],
            padding_bottom=["0em", "0em", "10em", "10em", "10em", "10em"],
        ),
        width="100%",
        class_name="bg-slate-1",
    )
