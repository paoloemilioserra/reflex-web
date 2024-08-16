import reflex as rx


@rx.memo
def h1_title(title: str) -> rx.Component:
    return rx.el.h1(
        title,
        class_name="inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full font-x-large md:font-xxx-large text-balance text-start text-transparent md:text-center",
    )
