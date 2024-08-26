import reflex as rx
from pcweb.components.icons import get_icon
from pcweb.components.webpage.comps import h1_title
from pcweb.flexdown import xd2 as xd


def back(title, url):
    def create_linkedin_share_url(path):
        """Create a LinkedIn share URL."""
        encoded_url = "https://reflex.dev" + (
            path if path.startswith("/") else "/" + path
        )
        encoded_url = encoded_url.replace(":", "%3A").replace("/", "%2F") + (
            "" if encoded_url.endswith("%2F") else "%2F"
        )
        return f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"

    return rx.flex(
        rx.link(
            "<- Back to Blog",
            color="var(--c-slate-9)",
            margin_bottom="2em",
            underline="hover",
            href="/blog",
        ),
        rx.link(
            rx.image(src="/companies/dark/twitter.svg", height="2em"),
            href=f"https://twitter.com/intent/tweet?text={title}&url=https://reflex.dev{url}&via=getreflex",
        ),
        rx.link(
            rx.image(src="/companies/dark/linkedin.svg", height="2em"),
            href=create_linkedin_share_url(url),
            is_external=True,
        ),
        rx.link(
            rx.image(src="/companies/dark/yc.svg", height="2em"),
            href=f"https://news.ycombinator.com/submitlink?u=https://reflex.dev{url}&t={title}",
            is_external=True,
        ),
        rx.link(
            rx.image(src="/companies/dark/reddit.svg", height="2em"),
            href=f"https://www.reddit.com/submit?url=https://reflex.dev{url}&title={title}",
            is_external=True,
        ),
        display=["none", "none", "none", "none", "flex", "flex"],
        spacing="2",
        direction="column",
        z_index=1,
        position="fixed",
        top="300px",
        left="15px",
        margin=0,
        width="auto",
    )


def page(document, route) -> rx.Component:
    """Create a page."""
    meta = document.metadata
    return rx.el.section(
        # back(meta["title"], route),
        rx.el.article(
            rx.link(
                rx.box(
                    get_icon("arrow_right", class_name="rotate-180"),
                    "Back to Blog",
                    class_name="box-border flex justify-center items-center gap-2 border-slate-5 bg-slate-1 hover:bg-slate-3 px-3 py-[0.125rem] border rounded-full font-small text-slate-9 transition-bg cursor-pointer -mb-4",
                ),
                underline="none",
                href="/blog",
            ),
            rx.el.header(
                h1_title(title=meta["title"]),
                rx.el.h2(
                    str(meta["description"]),
                    class_name="font-md text-balance text-slate-10",
                ),
                rx.box(
                    rx.text(
                        meta["author"],
                    ),
                    rx.text(
                        "·",
                    ),
                    rx.moment(
                        str(meta["date"]),
                        format="MMM DD, YYYY",
                    ),
                    class_name="flex items-center gap-2 font-small text-nowrap text-slate-9 !font-normal",
                ),
                class_name="section-header",
            ),
            rx.image(
                src=f"{meta['image']}",
                alt=f"Image for blog post: {meta['title']}",
                loading="lazy",
                class_name="rounded-[1.125rem] w-auto h-[22.5rem] object-center object-cover",
            ),
            rx.box(
                xd.render(document, "blog.md"),
                class_name="flex flex-col gap-4 max-w-2xl markdown-code",
            ),
            class_name="flex flex-col justify-center items-center gap-12",
        ),
        class_name="section-content",
    )
