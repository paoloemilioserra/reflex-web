"""Template for documentation pages."""

import reflex as rx
from pcweb import styles
from pcweb.styles import font_weights as fw
from pcweb.styles.colors import c_color
from pcweb.styles import fonts

icon_margins = {
    "h1": "10px",
    "h2": "5px",
    "h3": "2px",
    "h4": "0px",
}


def h_comp_common(
    text: rx.Var[str],
    heading: str,
    convert_to_str: bool = False,
    style: dict = {},
    class_name: str = "",
) -> rx.Component:
    if convert_to_str:
        id_ = text.to(list[str])[0].lower().split().join("-")
    else:
        id_ = text.lower().split().join("-")
    href = rx.State.router.page.full_path + "#" + id_

    return rx.link(
        rx.heading(
            text,
            id=id_,
            as_=heading,
            style=style,
            class_name=class_name,
        ),
        rx.icon(
            tag="link",
            size=18,
            class_name="!text-violet-9 invisible transition-[visibility_0.075s_ease-out] group-hover:visible",
        ),
        underline="none",
        href=href,
        on_click=lambda: rx.set_clipboard(href),
        # as_child=True,
        class_name="flex flex-row scroll-m-6 items-center gap-6 hover:!text-violet-9 text-slate-12 cursor-pointer mb-6 transition-colors group",
    )


@rx.memo
def h1_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        # style={
        #     # "color": c_color("slate", 12),
        #     "font-size": ["32px", "48px"],
        #     "font-style": "normal",
        #     "font-weight": "600",
        #     "line-height": ["48px", "56px"],
        #     "letter-spacing": "-2.4px",
        # },
        # margin_bottom="24px",
        # scroll_margin="4em",
        class_name="font-xx-large",
    )


@rx.memo
def h1_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h1",
        # style=fonts.xx_large,
        # margin_bottom="24px",
        # margin_top="1.5em",
        # scroll_margin="4em",
        convert_to_str=True,
        class_name="font-xx-large",
    )


@rx.memo
def h2_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        # style=fonts.x_large,
        # margin_bottom="24px",
        # margin_top=["24px", "40px"],
        # scroll_margin="5em",
        class_name="font-x-large",
    )


@rx.memo
def h2_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h2",
        # style=fonts.x_large,
        # margin_bottom="24px",
        # margin_top="0px",
        # scroll_margin="5em",
        convert_to_str=True,
        class_name="font-x-large",
    )


@rx.memo
def h3_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        # font_size=styles.H4_FONT_SIZE,
        # font_weight=fw["subheading"],
        # margin_top="1em",
        # margin_bottom="0em",
        # scroll_margin="5em",
        class_name="font-large",
    )


@rx.memo
def h3_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h3",
        # style=fonts.large,
        # margin_bottom="24px",
        # margin_top="24px",
        # scroll_margin="5em",
        convert_to_str=True,
        class_name="font-large",
    )


@rx.memo
def h4_comp(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        # font_size=styles.H4_FONT_SIZE,
        # font_weight=fw["subheading"],
        # margin_top="1em",
        scroll_margin="6em",
        class_name="font-md-smbold",
    )


@rx.memo
def h4_comp_xd(text: rx.Var[str]) -> rx.Component:
    return h_comp_common(
        text=text,
        heading="h4",
        # style=fonts.medium,
        # margin_bottom="24px",
        # scroll_margin="6em",
        convert_to_str=True,
        class_name="font-md-smbold",
    )
