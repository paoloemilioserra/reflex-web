import reflex as rx
from ..style import demo_height
from pcweb.components.button import button
import replicate

try:
    import openai

    openai_client = openai.OpenAI()
except:
    openai_client = None


class ImageGenState(rx.State):
    """The app state."""

    image_url = ""
    processing = False
    complete = False

    def get_image(self, form_data):
        """Get the image from the prompt."""
        prompt = form_data["prompt"]
        if prompt == "":
            return rx.toast("Prompt is empty")

        self.processing, self.complete = True, False
        yield
        input = {"prompt": prompt}

        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input=input,
        )
        self.image_url = output[0]
        self.processing, self.complete = False, True


def image_gen():
    return rx.box(
        rx.skeleton(
            rx.fragment(
                rx.cond(
                    ImageGenState.image_url,
                    rx.image(
                        src=ImageGenState.image_url,
                        class_name="rounded-lg w-auto max-w-full h-full max-h-full aspect-square flex-1",
                    ),
                    rx.box(
                        rx.icon("images", size=26, class_name="!text-slate-9"),
                        class_name="flex justify-center items-center border-slate-4 border rounded-lg w-full max-w-full h-full max-h-full bg-slate-1 flex-1",
                    ),
                ),
                loading=True,
            ),
        ),
        rx.form(
            rx.box(
                rx.el.input(
                    placeholder="What do you want to see?",
                    name="prompt",
                    type="text",
                    class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-white-1 p-[0.5rem_0.75rem] border rounded-[10px] font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none w-full",
                ),
                rx.form.submit(
                    button(
                        text=rx.cond(
                            ImageGenState.processing, "Generating...", "Generate"
                        ),
                        style={
                            "input:placeholder-shown + &": {
                                "opacity": "0.65",
                                "cursor": "default",
                                "_hover": {
                                    "background": "linear-gradient(180deg, var(--violet-9) 0%, var(--violet-10) 100%)"
                                },
                            },
                        },
                    ),
                    as_child=True,
                ),
                class_name="flex flex-row gap-2 align-center",
            ),
            on_submit=ImageGenState.get_image,
        ),
        class_name="flex flex-col items-center gap-4 p-10",
    )
