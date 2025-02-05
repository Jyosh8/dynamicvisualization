import typing as t
from pathlib import Path

from _typeshed import Incomplete
from flask import Flask

from .config import Config
from .extension.library import ElementLibrary
from .page import Page
from .partial import Partial
from .state import State

class Gui:
    on_action: Incomplete
    on_change: Incomplete
    on_init: Incomplete
    on_page_load: Incomplete
    on_navigate: Incomplete
    on_exception: Incomplete
    on_status: Incomplete
    on_user_content: Incomplete
    def __init__(
        self,
        page: str | Page | None = None,
        pages: dict | None = None,
        css_file: str | None = None,
        path_mapping: dict | None = None,
        env_filename: str | None = None,
        libraries: list[ElementLibrary] | None = None,
        flask: Flask | None = None,
    ) -> None: ...
    @staticmethod
    def add_library(library: ElementLibrary) -> None: ...
    @staticmethod
    def register_content_provider(
        content_type: type, content_provider: t.Callable[..., str]
    ) -> None: ...
    @staticmethod
    def add_shared_variable(*names: str) -> None: ...
    @staticmethod
    def add_shared_variables(*names: str) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ): ...
    def invoke_callback(
        self,
        state_id: str,
        callback: t.Callable | str,
        args: t.Sequence[t.Any] | None = None,
        module_context: str | None = None,
    ) -> t.Any: ...
    def broadcast_callback(
        self,
        callback: t.Callable,
        args: t.Sequence[t.Any] | None = None,
        module_context: str | None = None,
    ) -> dict[str, t.Any]: ...
    def broadcast_change(self, var_name: str, value: t.Any): ...
    def broadcast_changes(self, values: dict[str, t.Any] | None = None, **kwargs): ...
    def table_on_edit(self, state: State, var_name: str, payload: dict[str, t.Any]): ...
    def table_on_add(
        self,
        state: State,
        var_name: str,
        payload: dict[str, t.Any],
        new_row: list[t.Any] | None = None,
    ): ...
    def table_on_delete(
        self, state: State, var_name: str, payload: dict[str, t.Any]
    ): ...
    def add_page(self, name: str, page: str | Page, style: str | None = "") -> None: ...
    def add_pages(
        self, pages: t.Mapping[str, str | Page] | str | None = None
    ) -> None: ...
    def add_partial(self, page: str | Page) -> Partial: ...
    def load_config(self, config: Config) -> None: ...
    def get_flask_app(self) -> Flask: ...
    state: Incomplete
    def run(
        self,
        allow_unsafe_werkzeug: bool = ...,
        async_mode: str = ...,
        change_delay: t.Optional[int] = ...,
        chart_dark_template: t.Optional[t.Dict[str, t.Any]] = ...,
        base_url: t.Optional[str] = ...,
        client_url: t.Optional[str] = ...,
        dark_mode: bool = ...,
        dark_theme: t.Optional[t.Dict[str, t.Any]] = ...,
        data_url_max_size: t.Optional[int] = ...,
        debug: bool = ...,
        extended_status: bool = ...,
        favicon: t.Optional[str] = ...,
        flask_log: bool = ...,
        host: str = ...,
        light_theme: t.Optional[t.Dict[str, t.Any]] = ...,
        margin: t.Optional[str] = ...,
        ngrok_token: str = ...,
        notebook_proxy: bool = ...,
        notification_duration: int = ...,
        port: t.Union[t.Literal["auto"], int] = ...,
        port_auto_ranges: t.List[t.Union[int, t.Tuple[int, int]]] = ...,
        propagate: bool = ...,
        run_browser: bool = ...,
        run_in_thread: bool = ...,
        run_server: bool = ...,
        server_config: t.Optional[ServerConfig] = ...,
        single_client: bool = ...,
        state_retention_period: int = ...,
        stylekit: t.Union[bool, Stylekit] = ...,
        system_notification: bool = ...,
        theme: t.Optional[t.Dict[str, t.Any]] = ...,
        time_zone: t.Optional[str] = ...,
        title: t.Optional[str] = ...,
        upload_folder: t.Optional[str] = ...,
        use_arrow: bool = ...,
        use_reloader: bool = ...,
        watermark: t.Optional[str] = ...,
        webapp_path: t.Optional[str] = ...,
    ) -> Flask | None: ...
    def reload(self) -> None: ...
    def stop(self) -> None: ...
    def set_favicon(self, favicon_path: str | Path, state: State | None = None): ...
