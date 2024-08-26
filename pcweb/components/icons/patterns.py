import reflex as rx
from pcweb.components.icons.icons import get_icon



def create_pattern(
    pattern: str,
    class_name: str,
) -> rx.Component:
    return get_icon(
        pattern,
        class_name="absolute overflow-hidden pointer-events-none shrink-0"
        + " "
        + class_name,
    )


def landing_patterns() -> rx.Component:
    return [
        create_pattern(
            "radial_small",
            class_name="left-[-43px] top-[0px]",
        ),
        create_pattern(
            "radial_big",
            class_name="left-[-43px] top-[93px] scale-x-[-1] scale-y-[-1] rotate-180",
        ),
    ]
