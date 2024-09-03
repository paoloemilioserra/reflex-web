import reflex as rx


def companies() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                class_name="bg-gradient-to-r from-slate-2 to-slate-4 w-[12.5rem] h-[0.125rem] to-85%"
            ),
            rx.el.span(
                "Trusted by industry leading teams",
                class_name="font-small text-slate-9 px-2 py-[0.125rem]",
            ),
            rx.box(
                class_name="bg-gradient-to-r from-slate-4 to-slate-2 w-[12.5rem] h-[0.125rem] from-15%"
            ),
            class_name="flex flex-row items-center w-full justify-center",
        ),
        class_name="flex flex-col gap-6 pt-4 w-full justify-center",
    )
