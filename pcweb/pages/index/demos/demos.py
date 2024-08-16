
import reflex as rx

from .auth.auth import auth
from .forms.forms import forms
from .dashboard.dashboard import dashboard
from .image_gen.image_gen import image_gen
from reflex_type_animation import type_animation

class DemoState(rx.State):

    demo = "Image Generator"

    def set_demo(self, demo):
        self.demo = demo

def example_button(text):
    return rx.button(
    text,
    border_radius="8px;",
    border="1px solid var(--c-slate-5);",
    color=rx.cond(
        DemoState.demo == text,
        "white",
        "var(--c-slate-9)",
    ),
    background= rx.cond(
        DemoState.demo == text,
        "var(--c-violet-9)",
        "var(--c-slate-2)",
    ),
    backdrop_filter= "blur(2px);",
    on_click= lambda: DemoState.set_demo(text)
)

def heading():
    return rx.vstack(
        type_animation(
            sequence=[
                "Build web apps, faster.",
                1000,
                "Build internal tools, faster.",
                1000,
                "Build AI apps, faster.",
                1000,
                "Build web apps, faster.",
            ],
            font_size=["24px", "30px", "44px", "44px", "44px", "44px"],
            text_align="left",
            color="var(--c-slate-11)",
            font_weight="bold",
            line_height="1",
        ),
        rx.el.h3(
            "Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend.", 
            color="var(--c-slate-10)",
            font_size=[".8em", ".8em", "1em", "1em", "1em", "1em"],
            text_align="center",
            class_name="font-small"
        ),
        padding_y="1em",
    )
 
def more_examples():
    return rx.link(
                rx.button(
                    "More Examples", 
                    rx.icon(
                        "chevron-right", 
                        size=18,
                        stroke_width="1px",
                        padding_left=".1em",
                    ),   
                    background="var(--c-slate-2)",
                    color="var(--c-slate-9)",
                    border_radius="8px;",
                    border="1px solid var(--c-slate-5);",
                    text_wrap="nowrap",
                ),
                href="/gallery",
            )

def demos():
    return rx.flex(
        heading(),
        rx.hstack(
            rx.hstack(
                example_button("Image Gen"),
                example_button("Forms"),
                example_button("Auth"),
                example_button("Dashboard"),
                max_width="35em", 
                overflow_x="scroll",
                scrollbar_width= "none"
            ),
            rx.spacer(),
            more_examples(),
            align_items="left",
            width="100%",
        ),
        rx.box(
            rx.match(
                DemoState.demo,
                ("Forms", forms()),
                ("Dashboard", dashboard()),
                ("Auth", auth()),
                ("Image Generator", image_gen()),
                image_gen()
            ),
            border_radius= "10px;",
            border= "1px solid var(--c-slate-5);",
            background_color= "var(--c-slate-2)",
            overflow="hidden",
            width="100%",  
        ),
        padding_bottom="4em",
        width="100%",
        direction="column",
        # background_image="url(/grid.png)",
        background_position= ["50% 50%;", "50% 40%;", "50% 70%;", "50% 70%;", "50% 70%;", "50% 70%;"],
        background_repeat= "no-repeat;",
        background_size= "auto;",
        padding_top="5em",
        gap="1em",
        class_name="bg-slate-1"
    )

 