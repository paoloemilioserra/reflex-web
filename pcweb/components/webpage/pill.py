import reflex as rx

@rx.memo
def pill(text: str) -> rx.Component:
    return rx.box(
        text,
        class_name="border-violet-5 bg-violetA-3 px-3 py-1 border rounded-full font-small text-violet-9",
    )
