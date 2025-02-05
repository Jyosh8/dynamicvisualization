from datetime import datetime
from importlib.util import find_spec
from typing import Any, Callable, Optional, Union

from .. import Icon
from ._element import _Block, _Control
from ._element import content as content
from ._element import html as html
from .page import Page as Page

if find_spec("taipy.core"):
    from taipy.core import Cycle, DataNode, Job, Scenario

class text(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Any = "",
        *,
        raw: bool = False,
        mode: Optional[str] = None,
        format: Optional[str] = None,
        width: Optional[Union[str, int]] = None,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a text element.\n\nParameters\n----------\n\nvalue (dynamic)\n  The value displayed as text by this control.\n\nraw\n  If set to True, the component renders as an HTML <span> element without any default style.\n\nmode\n  Define the way the text is processed:\n  \n  * "raw": synonym for setting the *raw* property to True\n  * "pre": keeps spaces and new lines\n  * "markdown" or "md": basic support for Markdown.\n  \n\nformat\n  The format to apply to the value.\n\nwidth\n  The width of the element.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-text` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class button(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        label: Union[str, Icon] = "",
        *,
        on_action: Optional[Union[str, Callable]] = None,
        width: Optional[Union[str, int]] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a button element.\n\nParameters\n----------\n\nlabel (dynamic)\n  The label displayed in the button.\n\non_action\n  A function or the name of a function that is triggered when the button is pressed.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the button it it has one.\n  * payload (dict): a dictionary that contains the key "action" set to the name of the action that triggered this callback.\n  \n\nwidth\n  The width of the button element.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-button` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class input(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[Any] = None,
        *,
        password: bool = False,
        label: Optional[str] = None,
        multiline: bool = False,
        lines_shown: int = 5,
        type: str = "text",
        change_delay: Optional[int] = None,
        on_action: Optional[Union[str, Callable]] = None,
        action_keys: str = "Enter",
        width: Optional[Union[str, int]] = None,
        on_change: Optional[Union[str, Callable]] = None,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates an input element.\n\nParameters\n----------\n\nvalue (dynamic)\n  The value represented by this control.\n\npassword\n  If True, the text is obscured: all input characters are displayed as an asterisk ('*').\n\nlabel\n  The label associated with the input.\n\nmultiline\n  If True, the text is presented as a multi line input.\n\nlines_shown\n  The number of lines shown in the input control, when multiline is True.\n\ntype\n  The type of generated input HTML element, as defined in [HTML input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types).  \n  This value forces certain values to be entered and can be set to "text", "tel", "email", "url"..., among other choices.\n\nchange_delay\n  Minimum interval between two consecutive calls to the `on_change` callback.  \n  The default value is defined at the application configuration level by the **change_delay** configuration option.  \n  if None, the delay is set to 300 ms.  \n  If set to -1, the input change is triggered only when the user presses the Enter key.\n\non_action\n  A function or the name of a function that is triggered when a specific key is pressed.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the control if it has one.\n  * payload (dict): the details on this callback's invocation.  \n    \n    This dictionary has the following keys:\n    + action: the name of the action that triggered this callback.\n    + args (list):\n      - key name\n      - variable name\n      - current value\n  \n\naction_keys\n  Semicolon (';')-separated list of supported key names.  \n  Authorized values are Enter, Escape, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12.\n\nwidth\n  The width of the element.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-input` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class number(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[Any] = None,
        *,
        label: Optional[str] = None,
        step: Union[int, float] = 1,
        step_multiplier: Union[int, float] = 10,
        min: Optional[Union[int, float]] = None,
        max: Optional[Union[int, float]] = None,
        change_delay: Optional[int] = None,
        on_action: Optional[Union[str, Callable]] = None,
        action_keys: str = "Enter",
        width: Optional[Union[str, int]] = None,
        on_change: Optional[Union[str, Callable]] = None,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a number element.\n\nParameters\n----------\n\nvalue (dynamic)\n  The numerical value represented by this control.\n\nlabel\n  The label associated with the input.\n\nstep (dynamic)\n  The amount by which the value is incremented or decremented when the user clicks one of the arrow buttons.\n\nstep_multiplier (dynamic)\n  A factor that multiplies *step* when the user presses the Shift key while clicking one of the arrow buttons.\n\nmin (dynamic)\n  The minimum value to accept for this input.\n\nmax (dynamic)\n  The maximum value to accept for this input.\n\nchange_delay\n  Minimum interval between two consecutive calls to the `on_change` callback.  \n  The default value is defined at the application configuration level by the **change_delay** configuration option.  \n  if None, the delay is set to 300 ms.  \n  If set to -1, the input change is triggered only when the user presses the Enter key.\n\non_action\n  A function or the name of a function that is triggered when a specific key is pressed.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the control if it has one.\n  * payload (dict): the details on this callback's invocation.  \n    \n    This dictionary has the following keys:\n    + action: the name of the action that triggered this callback.\n    + args (list):\n      - key name\n      - variable name\n      - current value\n  \n\naction_keys\n  Semicolon (';')-separated list of supported key names.  \n  Authorized values are Enter, Escape, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12.\n\nwidth\n  The width of the element.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-number` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class slider(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[
            Union[int, float, str, list[int], list[float], list[str]]
        ] = None,
        *,
        min: Union[int, float] = 0,
        max: Union[int, float] = 100,
        step: Union[int, float] = 1,
        text_anchor: str = "bottom",
        labels: Optional[Union[bool, dict[str, str]]] = None,
        continuous: bool = True,
        change_delay: Optional[int] = None,
        width: str = "300px",
        height: Optional[str] = None,
        orientation: str = "horizontal",
        on_change: Optional[Union[str, Callable]] = None,
        lov: Optional[dict[str, Any]] = None,
        adapter: Optional[Union[str, Callable]] = None,
        type: Optional[str] = None,
        value_by_id: bool = False,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a slider element.\n\nParameters\n----------\n\nvalue (dynamic)\n  The value that is set for this slider.  \n  If this slider is based on a *lov* then this property can be set to the lov element.  \n  This value can also hold an array of numbers to indicate that the slider reflects a range (within the [*min*,*max*] domain) defined by several knobs that the user can set independently.  \n  If this slider is based on a *lov* then this property can be set to an array of lov elements. The slider is then represented with several knobs, one for each lov value.\n\nmin\n  The minimum value.  \n  This is ignored when *lov* is defined.\n\nmax\n  The maximum value.  \n  This is ignored when *lov* is defined.\n\nstep\n  The step value, which is the gap between two consecutive values the slider set. It is a good practice to have (*max*-*min*) being divisible by *step*.  \n  This property is ignored when *lov* is defined.\n\ntext_anchor\n  When the *lov* property is used, this property indicates the location of the label.  \n  Possible values are:\n  \n  * "bottom"\n  * "top"\n  * "left"\n  * "right"\n  * "none" (no label is displayed)\n  \n\nlabels\n  The labels for specific points of the slider.  \n  If set to True, this slider uses the labels of the *lov* if there are any.  \n  If set to a dictionary, the slider uses the dictionary keys as a *lov* key or index, and the associated value as the label.\n\ncontinuous\n  If set to False, the control emits an `on_change` notification only when the mouse button is released, otherwise notifications are emitted during the cursor movements.  \n  If *lov* is defined, the default value is False.\n\nchange_delay\n  Minimum time between triggering two `on_change` callbacks.  \n  The default value is defined at the application configuration level by the **change_delay** configuration option. if None or 0, there's no delay.\n\nwidth\n  The width of this slider, in CSS units.\n\nheight\n  The height of this slider, in CSS units.  \n  It defaults to the value of *width* when using the vertical orientation.\n\norientation\n  The orientation of this slider.  \n  Valid values are "horizontal" or "vertical".\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\nlov\n  The list of values. See the [section on List of Values](https://docs.taipy.io/en/release-4.0/manuals/userman/gui/viselements/generic/slider/../../../../../../userman/gui/binding/#list-of-values) for more details.\n\nadapter\n  A function or the name of the function that transforms an element of *lov* into a *tuple(id:str, label:Union[str,Icon])*.  \n  The default value is a function that returns the string representation of the *lov* element.\n\ntype\n  This property is required if *lov* contains a non-specific type of data (e.g., a dictionary).  \n  Then:\n  \n  * *value* must be of that type\n  * *lov* must be an iterable containing elements of this type\n  * The function set to *adapter* will receive an object of this type.\n  \n    \n  The default value is the type of the first element in *lov*.\n\nvalue_by_id\n  If False, the selection value (in *value*) is the selected element in *lov*. If set to True, then *value* is set to the id of the selected element in *lov*.\n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-slider` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class toggle(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[Any] = None,
        *,
        theme: bool = False,
        allow_unselect: bool = False,
        unselected_value: Optional[Any] = None,
        mode: Optional[str] = None,
        label: Optional[str] = None,
        width: Optional[Union[str, int]] = None,
        on_change: Optional[Union[str, Callable]] = None,
        lov: Optional[dict[str, Any]] = None,
        adapter: Optional[Union[str, Callable]] = None,
        type: Optional[str] = None,
        value_by_id: bool = False,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a toggle element.\n\nParameters\n----------\n\nvalue (dynamic)\n  Bound to the selection value.\n\ntheme\n  If set, this toggle control acts as a way to set the application Theme (dark or light).\n\nallow_unselect\n  If set, this allows de-selection and the value is set to unselected_value.\n\nunselected_value\n  Value assigned to *value* when no item is selected.\n\nmode\n  Define the way the toggle is displayed:\n  \n  * "theme": synonym for setting the *theme* property to True\n  \n\nlabel\n  The label associated with the toggle.\n\nwidth\n  The width of the element.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\nlov\n  The list of values. See the [section on List of Values](https://docs.taipy.io/en/release-4.0/manuals/userman/gui/viselements/generic/toggle/../../../../../../userman/gui/binding/#list-of-values) for more details.\n\nadapter\n  A function or the name of the function that transforms an element of *lov* into a *tuple(id:str, label:Union[str,Icon])*.  \n  The default value is a function that returns the string representation of the *lov* element.\n\ntype\n  This property is required if *lov* contains a non-specific type of data (e.g., a dictionary).  \n  Then:\n  \n  * *value* must be of that type\n  * *lov* must be an iterable containing elements of this type\n  * The function set to *adapter* will receive an object of this type.\n  \n    \n  The default value is the type of the first element in *lov*.\n\nvalue_by_id\n  If False, the selection value (in *value*) is the selected element in *lov*. If set to True, then *value* is set to the id of the selected element in *lov*.\n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-toggle` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class date(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        date: Optional[datetime] = None,
        *,
        with_time: bool = False,
        format: Optional[str] = None,
        editable: bool = True,
        label: Optional[str] = None,
        min: Optional[datetime] = None,
        max: Optional[datetime] = None,
        width: Optional[Union[str, int]] = None,
        on_change: Optional[Union[str, Callable]] = None,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a date element.\n\nParameters\n----------\n\ndate (dynamic)\n  The date that this control represents and can modify.  \n  It is typically bound to a `datetime` object.\n\nwith_time\n  Whether or not to show the time part of the date.\n\nformat\n  The format to apply to the value.\n\neditable (dynamic)\n  Shows the date as a formatted string if not editable.\n\nlabel\n  The label associated with the input.\n\nmin (dynamic)\n  The minimum date to accept for this input.\n\nmax (dynamic)\n  The maximum date to accept for this input.\n\nwidth\n  The width of the date element.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-date` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class date_range(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        dates: Optional[list[datetime]] = None,
        *,
        with_time: bool = False,
        format: Optional[str] = None,
        editable: bool = True,
        label_start: Optional[str] = None,
        label_end: Optional[str] = None,
        width: Optional[Union[str, int]] = None,
        on_change: Optional[Union[str, Callable]] = None,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a date_range element.\n\nParameters\n----------\n\ndates (dynamic)\n  The dates that this control represents and can modify.  \n  It is typically bound to a list of two `datetime` object.\n\nwith_time\n  Whether or not to show the time part of the date.\n\nformat\n  The format to apply to the value.\n\neditable (dynamic)\n  Shows the date as a formatted string if not editable.\n\nlabel_start\n  The label associated with the first input.\n\nlabel_end\n  The label associated with the second input.\n\nwidth\n  The width of the date_range element.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-date_range` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class chart(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        data: Optional[Any] = None,
        *,
        type: str = "scatter",
        mode: str = "lines+markers",
        x: Optional[str] = None,
        y: Optional[str] = None,
        z: Optional[str] = None,
        lon: Optional[str] = None,
        lat: Optional[str] = None,
        r: Optional[str] = None,
        theta: Optional[str] = None,
        high: Optional[str] = None,
        low: Optional[str] = None,
        open: Optional[str] = None,
        close: Optional[str] = None,
        measure: Optional[str] = None,
        locations: Optional[str] = None,
        values: Optional[str] = None,
        labels: Optional[str] = None,
        parents: Optional[str] = None,
        text: Optional[str] = None,
        base: Optional[str] = None,
        title: Optional[str] = None,
        render: bool = True,
        on_range_change: Optional[Union[str, Callable]] = None,
        columns: Optional[Union[str, list[str], dict[str, dict[str, str]]]] = None,
        label: Optional[str] = None,
        name: Optional[str] = None,
        selected: Optional[Union[list[int], str]] = None,
        color: Optional[str] = None,
        selected_color: Optional[str] = None,
        marker: Optional[dict[str, Any]] = None,
        line: Optional[Union[str, dict[str, Any]]] = None,
        selected_marker: Optional[dict[str, Any]] = None,
        layout: Optional[dict[str, Any]] = None,
        plot_config: Optional[dict[str, Any]] = None,
        options: Optional[dict[str, Any]] = None,
        orientation: Optional[str] = None,
        text_anchor: Optional[str] = None,
        xaxis: Optional[str] = None,
        yaxis: Optional[str] = None,
        width: Union[str, int, float] = "100%",
        height: Optional[Union[str, int, float]] = None,
        template: Optional[dict] = None,
        template__dark: Optional[dict] = None,
        template__light: Optional[dict] = None,
        decimator: Optional["taipy.gui.data.Decimator"] = None,
        rebuild: bool = False,
        figure: Optional["plotly.graph_objects.Figure"] = None,
        on_click: Optional[Union[str, Callable]] = None,
        on_change: Optional[Union[str, Callable]] = None,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a chart element.\n\nParameters\n----------\n\ndata (dynamic)\n  The data object bound to this chart control.  \n  See the section on the [*data* property](#the-data-property) below for more details.\n\ntype (indexed)\n  Chart type.  \n  See the Plotly [chart type](https://plotly.com/javascript/reference/) documentation for more details.\n\nmode (indexed)\n  Chart mode.  \n  See the Plotly [chart mode](https://plotly.com/javascript/reference/scatter/#scatter-mode) documentation for more details.\n\nx (indexed)\n  Column name for the *x* axis.\n\ny (indexed)\n  Column name for the *y* axis.\n\nz (indexed)\n  Column name for the *z* axis.\n\nlon (indexed)\n  Column name for the *longitude* value, for 'scattergeo' charts. See [Plotly Map traces](https://plotly.com/javascript/reference/scattergeo/#scattergeo-lon).\n\nlat (indexed)\n  Column name for the *latitude* value, for 'scattergeo' charts. See [Plotly Map traces](https://plotly.com/javascript/reference/scattergeo/#scattergeo-lat).\n\nr (indexed)\n  Column name for the *r* value, for 'scatterpolar' charts. See [Plotly Polar charts](https://plotly.com/javascript/polar-chart/).\n\ntheta (indexed)\n  Column name for the *theta* value, for 'scatterpolar' charts. See [Plotly Polar charts](https://plotly.com/javascript/polar-chart/).\n\nhigh (indexed)\n  Column name for the *high* value, for 'candlestick' charts. See [Plotly Candlestick charts](https://plotly.com/javascript/reference/candlestick/#candlestick-high).\n\nlow (indexed)\n  Column name for the *low* value, for 'candlestick' charts. See [Ploty Candlestick charts](https://plotly.com/javascript/reference/candlestick/#candlestick-low).\n\nopen (indexed)\n  Column name for the *open* value, for 'candlestick' charts. See [Plotly Candlestick charts](https://plotly.com/javascript/reference/candlestick/#candlestick-open).\n\nclose (indexed)\n  Column name for the *close* value, for 'candlestick' charts. See [Plotly Candlestick charts](https://plotly.com/javascript/reference/candlestick/#candlestick-close).\n\nmeasure (indexed)\n  Column name for the *measure* value, for 'waterfall' charts. See [Plotly Waterfall charts](https://plotly.com/javascript/reference/waterfall/#waterfall-measure).\n\nlocations (indexed)\n  Column name for the *locations* value. See [Plotly Choropleth maps](https://plotly.com/javascript/choropleth-maps/).\n\nvalues (indexed)\n  Column name for the *values* value. See [Plotly Pie charts](https://plotly.com/javascript/reference/pie/#pie-values) or [Plotly Funnel Area charts](https://plotly.com/javascript/reference/funnelarea/#funnelarea-values).\n\nlabels (indexed)\n  Column name for the *labels* value. See [Plotly Pie charts](https://plotly.com/javascript/reference/pie/#pie-labels).\n\nparents (indexed)\n  Column name for the *parents* value. See [Plotly Treemap charts](https://plotly.com/javascript/reference/treemap/#treemap-parents).\n\ntext (indexed)\n  Column name for the text associated to the point for the indicated trace.  \n  This is meaningful only when *mode* has the *text* option.\n\nbase (indexed)\n  Column name for the *base* value. Used in bar charts only.  \n  See the Plotly [bar chart base](https://plotly.com/javascript/reference/bar/#bar-base) documentation for more details."\n\ntitle\n  The title of this chart control.\n\nrender (dynamic)\n  If True, this chart is visible on the page.\n\non_range_change\n  A function or the name of a function that is triggered when the visible part of the x axis changes.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the chart control if it has one.\n  * payload (dict[str, Any]): the full details on this callback's invocation, as emitted by [Plotly](https://plotly.com/javascript/plotlyjs-events/#update-data).\n  \n\ncolumns\n  The list of column names to represent.\n  \n  * str: ;-separated list of column names\n  * list[str]: list of names\n  * dict: {"column_name": {format: "format", index: 1}} if index is specified, it represents the display order of the columns.\n    If not, the list order defines the index\n  \n    \n  If *columns* is omitted or set to None, all columns of *data* are represented.\n\nlabel (indexed)\n  The label for the indicated trace.  \n  This is used when the mouse hovers over a trace.\n\nname (indexed)\n  The name of the indicated trace.\n\nselected (dynamic) (indexed)\n  The list of the selected point indices .\n\ncolor (indexed)\n  The color of the indicated trace (or a column name for scattered).\n\nselected_color (indexed)\n  The color of the selected points for the indicated trace.\n\nmarker (indexed)\n  The type of markers used for the indicated trace.  \n  See [marker](https://plotly.com/javascript/reference/scatter/#scatter-marker) for more details.  \n  Color, opacity, size and symbol can be column names.\n\nline (indexed)\n  The configuration of the line used for the indicated trace.  \n  See [line](https://plotly.com/javascript/reference/scatter/#scatter-line) for more details.  \n  If the value is a string, it must be a dash type or pattern (see [dash style of lines](https://plotly.com/python/reference/scatter/#scatter-line-dash) for more details).\n\nselected_marker (indexed)\n  The type of markers used for selected points in the indicated trace.  \n  See [selected marker for more details.](https://plotly.com/javascript/reference/scatter/#scatter-selected-marker)\n\nlayout (dynamic)\n  The *plotly.js* compatible [layout object](https://plotly.com/javascript/reference/layout/).\n\nplot_config\n  The *plotly.js* compatible  [configuration options object](https://plotly.com/javascript/configuration-options/).\n\noptions (indexed)\n  The *plotly.js* compatible [data object where dynamic data will be overridden.](https://plotly.com/javascript/reference/).\n\norientation (indexed)\n  The orientation of the indicated trace.\n\ntext_anchor (indexed)\n  Position of the text relative to the point.  \n  Valid values are: *top*, *bottom*, *left*, and *right*.\n\nxaxis (indexed)\n  The *x* axis identifier for the indicated trace.\n\nyaxis (indexed)\n  The *y* axis identifier for the indicated trace.\n\nwidth\n  The width of this chart, in CSS units.\n\nheight\n  The height of this chart, in CSS units.\n\ntemplate\n  The Plotly [layout template](https://plotly.com/javascript/layout-template/).\n\ntemplate[dark]\n  The Plotly [layout template](https://plotly.com/javascript/layout-template/) applied over the base template when theme is dark.\n\ntemplate[light]\n  The Plotly [layout template](https://plotly.com/javascript/layout-template/) applied over the base template when theme is not dark.\n\ndecimator (indexed)\n  A decimator instance for the indicated trace that reduces the volume of the data being sent back and forth.  \n  If defined as *indexed*, it impacts only the indicated trace; if not, it applies to the first trace only.\n\nrebuild (dynamic)\n  Allows dynamic config refresh if set to True.\n\nfigure (dynamic)\n  A figure as produced by Plotly.\n\non_click\n  A function or the name of a function that is triggered when the user clicks in the chart background.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the chart control if it has one.\n  * payload (dict[str, Any]): a dictionary containing the *x* and *y* coordinates of the click **or** *latitude* and *longitude* in the case of a map. This feature relies on non-public Plotly structured information.\n  \n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-chart` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class table(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        data: Optional[Any] = None,
        *,
        page_size: int = 100,
        allow_all_rows: bool = False,
        show_all: bool = False,
        auto_loading: bool = False,
        width__column_name: Optional[str] = None,
        selected: Optional[Union[list[int], str]] = None,
        page_size_options: Union[list[int], str] = [50, 100, 500],
        columns: Optional[
            Union[str, list[str], dict[str, dict[str, Union[str, int]]]]
        ] = None,
        date_format: str = "MM/dd/yyyy",
        number_format: Optional[str] = None,
        group_by__column_name: bool = False,
        apply__column_name: str = "first",
        row_class_name: Optional[Union[str, Callable]] = None,
        cell_class_name__column_name: Optional[Union[str, Callable]] = None,
        tooltip: Optional[Union[str, Callable]] = None,
        tooltip__column_name: Optional[Union[str, Callable]] = None,
        format_fn__column_name: Optional[Union[str, Callable]] = None,
        width: str = "100%",
        height: str = "80vh",
        filter: bool = False,
        filter__column_name: bool = False,
        nan_value: str = "",
        nan_value__column_name: str = "",
        editable: bool = False,
        editable__column_name: Optional[bool] = None,
        on_edit: Optional[Union[bool, Callable]] = None,
        on_add: Optional[Union[bool, Callable]] = None,
        on_delete: Optional[Union[bool, Callable]] = None,
        on_action: Optional[Union[str, Callable]] = None,
        size: str = "small",
        rebuild: bool = False,
        lov__column_name: Optional[Union[list[str], str]] = None,
        downloadable: bool = False,
        on_compare: Optional[Union[str, Callable]] = None,
        use_checkbox: bool = False,
        sortable: bool = True,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a table element.\n\nParameters\n----------\n\ndata (dynamic)\n  The data to be represented in this table. This property can be indexed to define other data for comparison.\n\npage_size\n  For a paginated table, the number of visible rows.\n\nallow_all_rows\n  For a paginated table, adds an option to show all the rows.\n\nshow_all\n  For a paginated table, show all the rows.\n\nauto_loading\n  If True, the data will be loaded on demand.\n\nwidth[<i>column_name</i>]\n  The width of the indicated column, in CSS units (% values are not supported).\n\nselected (dynamic)\n  The list of the indices of the rows to be displayed as selected.\n\npage_size_options\n  The list of available page sizes that users can choose from.\n\ncolumns\n  The list of the column names to display.\n  \n  * str: semicolon (';')-separated list of column names.\n  * list[str]: the list of column names.\n  * dict: a dictionary with entries matching: {"<column_name>": {"format": "<format>", "index": 1}}.  \n    \n    if *index* is specified, it represents the display order of this column.\n    If *index* is not specified, the list order defines the index.  \n    \n    If *format* is specified, it is used for numbers or dates.\n  \n    \n  If *columns* is omitted or set to None, all columns of *data* are represented.\n\ndate_format\n  The date format used for all date columns when the format is not specifically defined.\n\nnumber_format\n  The number format used for all number columns when the format is not specifically defined.\n\ngroup_by[<i>column_name</i>]\n  Indicates, if True, that the given column can be aggregated.  \n  See [below](#aggregation) for more details.\n\napply[<i>column_name</i>]\n  The name of the aggregation function to use.  \n  This is used only if *group_by[column_name]* is set to True.  \n  See [below](#aggregation) for more details.\n\nrow_class_name\n  Allows for styling rows.  \n  This property must be a function or the name of a function that return the name of a CSS class for table rows.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *index* (int): the index of the row.\n  * *row* (Any): all the values for this row.\n  \n    \n  See [below](#dynamic-styling) for more details.\n\ncell_class_name[<i>column_name</i>]\n  Allows for styling cells.  \n  This property must be a function or the name of a function that return the name of a CSS class for table cells.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *value* (Any): the value of the cell.\n  * *index* (int): the index of the row.\n  * *row* (Any): all the values for this row.\n  * *column_name* (str): the name of the column.\n  \n    \n  See [below](#dynamic-styling) for more details.\n\ntooltip\n  Enables tooltips on cells.  \n  This property must be a function or the name of a function that must return a tooltip text for a cell.  \n  See [below](#cell-tooltips) for more details.\n\ntooltip[<i>column_name</i>]\n  Enables tooltips on cells at a column level.  \n  This property must be a function or the name of a the function that must return a tooltip text for a cell.  \n  See [below](#cell-tooltips) for more details.\n\nformat_fn[<i>column_name</i>]\n  Defines custom formatting for table cells. This property must be a function or the name of a function that returns a formatted string for each cell.  \n  The function is invoked when the cells in the specified column (*column_name*) are rendered. It should return a string that represents the cell value to provide the best user experience.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *value* (Any): the value of the cell.\n  * *index* (int): the index of the row.\n  * *row* (Any): the entire row. The type depends on the type of *data*.\n  * *column_name* (str): the name of the column.\n  \n  By default, no custom formatting is applied to the column.  \n  For more details, see the [section](#cell-formats).\n\nwidth\n  The width of this table control, in CSS units.\n\nheight\n  The height of this table control, in CSS units.\n\nfilter\n  Indicates, if True, that all columns can be filtered.\n\nfilter[<i>column_name</i>]\n  Indicates, if True, that the indicated column can be filtered.\n\nnan_value\n  The replacement text for NaN (not-a-number) values.\n\nnan_value[<i>column_name</i>]\n  The replacement text for NaN (not-a-number) values for the indicated column.\n\neditable (dynamic)\n  Indicates, if True, that all cells can be edited.\n\neditable[<i>column_name</i>]\n  Indicates, if False, that the indicated column cannot be edited, even if *editable* is True.  \n  By default, all columns are editable or not, depending on the value of the *editable* property.\n\non_edit\n  A function or the name of a function triggered when an edited cell is validated.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *var_name* (str): the name of the tabular data variable.\n  * *payload* (dict): a dictionary containing details about the callback invocation, with the following keys:\n    + *index* (int): the row index.\n    + *col* (str): the column name.\n    + *value* (Any): the new cell value, cast to the column's data type.\n    + *user_value* (str): the new cell value, as entered by the user.\n    + *tz* (str): the timezone, if the column type is `date`.\n  \n  If this property is set to False, the table does not provide the cell editing functionality.  \n  If this property is not set, the table will use the default implementation for editing cells.\n\non_add\n  A function or the name of a function that is triggered when the user requests a row to be added to the table.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *var_name* (str): the name of the tabular data variable.\n  * *payload* (dict): the details on this callback's invocation.  \n    This dictionary has the following key:\n    + *index* (int): the row index.\n  \n    \n  If this property is not set, the table uses the default implementation for adding a new row  \n  If this property is set to False, you cannot add new rows.\n\non_delete\n  A function or the name of a function triggered when a row is deleted.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *var_name* (str): the name of the tabular data variable.\n  * *payload* (dict): the details on this callback's invocation.  \n    \n    This dictionary has one key:\n    + *index* (int): the row index.\n  \n    \n  If this property is not set, the table uses the default implementation for deleting rows.\n\non_action\n  A function or the name of a function that is triggered when the user selects a row.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the name of the tabular data variable.\n  * payload (dict): the details on this callback's invocation.  \n    This dictionary has the following keys:\n    + action: the name of the action that triggered this callback.\n    + index (int): the row index.\n    + col (str): the column name.\n    + reason (str): the origin of the action: "click", or "button" if the cell contains a Markdown link syntax.\n    + value (str): the *link value* indicated in the cell when using a Markdown link syntax (that is, *reason* is set to "button").\n  \n  .\n\nsize\n  The size of the rows.  \n  Valid values are "small" and "medium".\n\nrebuild (dynamic)\n  If set to True, this allows to dynamically refresh the columns.\n\nlov[<i>column_name</i>]\n  The list of values of the indicated column.\n\ndownloadable\n  If True, a clickable icon is shown so the user can download the data as CSV.\n\non_compare\n  A function or the name of a function that compares data. This function should return a structure that identifies the differences between the different data passed as name. The default implementation compares the default data with the data[1] value.\n\nuse_checkbox\n  If True, boolean values are rendered as a simple HTML checkbox.\n\nsortable\n  If False, the table provides no sorting capability. Individual columns can override this global setting, allowing specific columns to be marked as sortable or non-sortable regardless of value of *sortable*, by setting the *sortable* property to True or False accordingly, in the dictionary for that column in the *columns* property value.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-table` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class selector(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        label: Optional[str] = None,
        *,
        mode: Optional[str] = None,
        dropdown: bool = False,
        multiple: bool = False,
        filter: bool = False,
        width: Union[str, int] = "360px",
        height: Optional[Union[str, int]] = None,
        value: Optional[Any] = None,
        on_change: Optional[Union[str, Callable]] = None,
        lov: Optional[dict[str, Any]] = None,
        adapter: Optional[Union[str, Callable]] = None,
        type: Optional[str] = None,
        value_by_id: bool = False,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a selector element.\n\nParameters\n----------\n\nvalue (dynamic)\n  Bound to the selection value.\n\nlabel\n  The label associated with the selector when in dropdown mode.\n\nmode\n  Define the way the selector is displayed:\n  \n  * "radio": as a list of radio buttons\n  * "check": as a list of check boxes\n  * any other value: a plain list.\n  \n\ndropdown\n  If True, the list of items is shown in a dropdown menu.  \n    \n  You cannot use the filter in that situation.\n\nmultiple\n  If True, the user can select multiple items.\n\nfilter\n  If True, this control is combined with a filter input area.\n\nwidth\n  The width of this selector, in CSS units.\n\nheight\n  The height of this selector, in CSS units.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\nlov\n  The list of values. See the [section on List of Values](https://docs.taipy.io/en/release-4.0/manuals/userman/gui/viselements/generic/selector/../../../../../../userman/gui/binding/#list-of-values) for more details.\n\nadapter\n  A function or the name of the function that transforms an element of *lov* into a *tuple(id:str, label:Union[str,Icon])*.  \n  The default value is a function that returns the string representation of the *lov* element.\n\ntype\n  This property is required if *lov* contains a non-specific type of data (e.g., a dictionary).  \n  Then:\n  \n  * *value* must be of that type\n  * *lov* must be an iterable containing elements of this type\n  * The function set to *adapter* will receive an object of this type.\n  \n    \n  The default value is the type of the first element in *lov*.\n\nvalue_by_id\n  If False, the selection value (in *value*) is the selected element in *lov*. If set to True, then *value* is set to the id of the selected element in *lov*.\n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-selector` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class file_download(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        content: Optional[Union[path, file, URL, ReadableBuffer, None]] = None,
        *,
        label: Optional[str] = None,
        on_action: Optional[Union[str, Callable]] = None,
        auto: bool = False,
        render: bool = True,
        bypass_preview: bool = True,
        name: Optional[str] = None,
        width: Optional[Union[str, int]] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a file_download element.\n\nParameters\n----------\n\ncontent (dynamic)\n  The content to transfer.  \n  If this is a string, a URL, or a file, then the content is read from this source.  \n  If a readable buffer is provided (such as an array of bytes...), and to prevent the bandwidth from being consumed too much, the way the data is transferred depends on the *data_url_max_size* parameter of the application configuration (which is set to 50kB by default):\n  \n  * If the buffer size is smaller than this setting, then the raw content is generated as a data URL, encoded using base64 (i.e. `"data:<mimetype>;base64,<data>"`).\n  * If the buffer size exceeds this setting, then it is transferred through a temporary file.\n  \n  If this property is set to None, that indicates that dynamic content is generated. Please take a look at the examples below for more details on dynamic generation.\n\nlabel (dynamic)\n  The label of the button.\n\non_action\n  A function or the name of a function that is triggered when the download is terminated (or on user action if *content* is None).  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the button if it has one.\n  * payload (dict): the details on this callback's invocation.  \n    \n    This dictionary has two keys:\n    + action: the name of the action that triggered this callback.\n    + args: a list of two elements: *args[0]* reflects the *name* property and *args[1]* holds the file URL.\n  \n\nauto\n  If True, the download starts as soon as the page is loaded.\n\nrender (dynamic)\n  If True, the control is displayed.  \n  If False, the control is not displayed.\n\nbypass_preview\n  If False, allows the browser to try to show the content in a different tab.  \n  The file download is always performed.\n\nname\n  A name proposition for the file to save, that the user can change.\n\nwidth\n  The width of the element.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-file_download` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class file_selector(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        content: Optional[str] = None,
        *,
        label: Optional[str] = None,
        on_action: Optional[Union[str, Callable]] = None,
        multiple: bool = False,
        extensions: str = ".csv,.xlsx",
        drop_message: str = "Drop here to Upload",
        notify: bool = True,
        width: Optional[Union[str, int]] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a file_selector element.\n\nParameters\n----------\n\ncontent (dynamic)\n  The path or the list of paths of the uploaded files.\n\nlabel\n  The label of the button.\n\non_action\n  A function or the name of a function that will be triggered.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the button if it has one.\n  * payload (dict): a dictionary that contains the key "action" set to the name of the action that triggered this callback.\n  \n\nmultiple\n  If set to True, multiple files can be uploaded.\n\nextensions\n  The list of file extensions that can be uploaded.\n\ndrop_message\n  The message that is displayed when the user drags a file above the button.\n\nnotify\n  If set to False, the user won't be notified of upload finish.\n\nwidth\n  The width of the element.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-file_selector` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class image(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        content: Optional[Union[path, URL, file, ReadableBuffer]] = None,
        *,
        label: Optional[str] = None,
        on_action: Optional[Union[str, Callable]] = None,
        width: Union[str, int, float] = "300px",
        height: Optional[Union[str, int, float]] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates an image element.\n\nParameters\n----------\n\ncontent (dynamic)\n  The image source.  \n  If a buffer is provided (string, array of bytes...), and in order to prevent the bandwidth to be consumed too much, the way the image data is transferred depends on the *data_url_max_size* parameter of the application configuration (which is set to 50kB by default):\n  \n  * If the size of the buffer is smaller than this setting, then the raw content is generated as a\n    data URL, encoded using base64 (i.e. `"data:<mimetype>;base64,<data>"`).\n  * If the size of the buffer is greater than this setting, then it is transferred through a temporary\n    file.\n  \n\nlabel (dynamic)\n  The label for this image.\n\non_action\n  A function or the name of a function that is triggered when the user clicks on the image.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the button if it has one.\n  * payload (dict): a dictionary that contains the key "action" set to the name of the action that triggered this callback.\n  \n\nwidth\n  The width of this image control, in CSS units.\n\nheight\n  The height of this image control, in CSS units.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-image` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class metric(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[Union[int, float]] = None,
        *,
        type: str = "circular",
        min: Union[int, float] = 0,
        max: Union[int, float] = 100,
        delta: Optional[Union[int, float]] = None,
        delta_color: Optional[str] = None,
        title: Optional[str] = None,
        negative_delta_color: Optional[str] = None,
        threshold: Optional[Union[int, float]] = None,
        show_value: bool = True,
        format: Optional[str] = None,
        delta_format: Optional[str] = None,
        bar_color: Optional[str] = None,
        color_map: Optional[dict] = None,
        width: Union[str, number] = "20vw",
        height: Union[str, number] = "20vh",
        layout: Optional[dict[str, Any]] = None,
        template: Optional[dict] = None,
        template__dark: Optional[dict] = None,
        template__light: Optional[dict] = None,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a metric element.\n\nParameters\n----------\n\nvalue (dynamic)\n  The value to represent.\n\ntype\n  The type of the gauge.  \n  Possible values are:\n  \n  * "none"\n  * "circular"\n  * "linear"\n  \n  Setting this value to "none" remove the gauge.\n\nmin\n  The minimum value of this metric control's gauge.\n\nmax\n  The maximum value of this metric control's gauge.\n\ndelta (dynamic)\n  The delta value to display.\n\ndelta_color\n  The color that is used to display the value of the *delta* property.  \n  If *negative_delta_color* is set, then this property applies for positive values of *delta* only.  \n  If this property is set to "invert", then values for *delta* are represented with the color used for negative values if delta is positive and *delta* is represented with the color used for positive values if it is negative.\n\ntitle\n  The title of the metric.\n\nnegative_delta_color\n  If set, this represents the color to be used when the value of *delta* is negative (or positive if *delta_color* is set to "invert").\n\nthreshold (dynamic)\n  The threshold value to display.\n\nshow_value\n  If set to False, the value is not displayed.\n\nformat\n  The format to use when displaying the value.  \n  This uses the `printf` syntax.\n\ndelta_format\n  The format to use when displaying the delta value.  \n  This uses the `printf` syntax.\n\nbar_color\n  The color of the bar in the gauge.\n\ncolor_map\n  Indicates what colors should be used for different ranges of the metric. The *color_map*'s keys represent the lower bound of each range, which is a number, while the values represent the color for that range.  \n  If the value associated with a key is set to None, the corresponding range is not assigned any color.\n\nwidth\n  The width of the metric control, in CSS units\n\nheight\n  The height of the metric control, in CSS units\n\nlayout (dynamic)\n  The *plotly.js* compatible [layout object](https://plotly.com/javascript/reference/layout/).\n\ntemplate\n  The Plotly [layout template](https://plotly.com/javascript/layout-template/).\n\ntemplate[dark]\n  The Plotly [layout template](https://plotly.com/javascript/layout-template/) applied over the base template when theme is dark.\n\ntemplate[light]\n  The Plotly [layout template](https://plotly.com/javascript/layout-template/) applied over the base template when theme is not dark.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-metric` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class progress(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[int] = None,
        *,
        linear: bool = False,
        show_value: bool = False,
        title: Optional[str] = None,
        title_anchor: str = "bottom",
        render: bool = True,
        width: Optional[Union[str, int]] = None,
    ) -> None:
        """Creates a progress element.\n\nParameters\n----------\n\nvalue (dynamic)\n  The progress percentage represented by the control.  \n  If this property is not set or set to None, the progress control represents an indeterminate state.\n\nlinear\n  If set to True, the control displays a linear progress indicator instead of a circular one.\n\nshow_value\n  If set to True, the progress value is shown.\n\ntitle (dynamic)\n  The title of the progress indicator.\n\ntitle_anchor\n  The anchor of the title.  \n  Possible values are:\n  \n  * "bottom"\n  * "top"\n  * "left"\n  * "right"\n  * "none" (no title is displayed)\n  \n\nrender (dynamic)\n  If False, this progress indicator is hidden from the page.\n\nwidth\n  The width of this progress indicator, in CSS units.\n\n"""  # noqa: E501
        ...

class indicator(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        display: Optional[Any] = None,
        *,
        value: Optional[Union[int, float]] = None,
        min: Union[int, float] = 0,
        max: Union[int, float] = 100,
        format: Optional[str] = None,
        orientation: str = "horizontal",
        width: Optional[str] = None,
        height: Optional[str] = None,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
    ) -> None:
        """Creates an indicator element.\n\nParameters\n----------\n\ndisplay (dynamic)\n  The label to be displayed.  \n  This can be formatted if it is a numerical value.\n\nvalue (dynamic)\n  The location of the label on the [*min*, *max*] range.  \n  The default value is the *min* value.\n\nmin\n  The minimum value of the range.\n\nmax\n  The maximum value of the range.\n\nformat\n  The format to use when displaying the value.  \n  This uses the `printf` syntax.\n\norientation\n  The orientation of this slider.\n\nwidth\n  The width of the indicator, in CSS units (used when orientation is horizontal).\n\nheight\n  The height of the indicator, in CSS units (used when orientation is vertical).\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-indicator` class name.\n\n"""  # noqa: E501
        ...

class menu(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        lov: Optional[Union[str, list[Union[str, Icon, Any]]]] = None,
        *,
        adapter: Optional[Union[str, Callable]] = None,
        type: Optional[str] = None,
        label: Optional[str] = None,
        inactive_ids: Optional[Union[str, list[str]]] = None,
        width: str = "15vw",
        width__mobile: str = "85vw",
        on_action: Optional[Union[str, Callable]] = None,
        active: bool = True,
    ) -> None:
        """Creates a menu element.\n\nParameters\n----------\n\nlov (dynamic)\n  The list of menu option values.\n\nadapter\n  A function or the name of the function that transforms an element of *lov* into a *tuple(id:str, label:Union[str,Icon])*.  \n  The default value is a function that returns the string representation of the *lov* element.\n\ntype\n  This property is required if *lov* contains a non-specific type of data (e.g., a dictionary).  \n  Then:\n  \n  * *value* must be of that type\n  * *lov* must be an iterable containing elements of this type\n  * The function set to *adapter* will receive an object of this type.\n  \n    \n  The default value is the type of the first element in *lov*.\n\nlabel\n  The title of the menu.\n\ninactive_ids (dynamic)\n  Semicolon (';')-separated list or a list of menu items identifiers that are disabled.\n\nwidth\n  The width of the menu when unfolded, in CSS units.  \n  Note that when running on a mobile device, the property *width[active]* is used instead.\n\nwidth[mobile]\n  The width of the menu when unfolded, in CSS units, when running on a mobile device.\n\non_action\n  A function or the name of a function that is triggered when a menu option is selected.  \n    \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the button, if it has one.\n  * payload (dict): a dictionary containing details about the callback invocation, with the following keys:\n    + action: the name of the action that triggered this callback.\n    + args: a list where the first element contains the identifier of the selected option.\n  \n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\n"""  # noqa: E501
        ...

class navbar(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        lov: Optional[dict[str, Any]] = None,
        *,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a navbar element.\n\nParameters\n----------\n\nlov\n  The list of pages. The keys should be:\n  \n  * page id (start with "/")\n  * or full URL\n  \n  The values are labels. See the [section on List of Values](https://docs.taipy.io/en/release-4.0/manuals/userman/gui/viselements/generic/navbar/../../../../../../userman/gui/binding/#list-of-values) for more details.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-navbar` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class status(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        value: Optional[Union[tuple, dict, list[dict], list[tuple]]] = None,
        *,
        without_close: bool = False,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a status element.\n\nParameters\n----------\n\nvalue\n  The different status items to represent.\n\nwithout_close\n  If True, the user cannot remove the status items from the list.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-status` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class login(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        title: str = "Log in",
        *,
        on_action: Optional[Union[str, Callable]] = None,
        message: Optional[str] = None,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a login element.\n\nParameters\n----------\n\ntitle\n  The title of the login dialog.\n\non_action\n  A function or the name of a function that is triggered when the dialog button is pressed.  \n    \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the button if it has one.\n  * payload (dict): the details on this callback's invocation.  \n    \n    This dictionary has the following keys:\n    + action: the name of the action that triggered this callback.\n    + args: a list with three elements:\n      - The first element is the username\n      - The second element is the password\n      - The third element is the current page name\n  \n    \n  When the button is pressed, and if this property is not set, Taipy will try to find a callback function called *on_login()* and invoke it with the parameters listed above.\n\nmessage (dynamic)\n  The message shown in the dialog.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-login` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class chat(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        messages: Optional[list[str]] = None,
        *,
        users: Optional[list[Union[str, Icon]]] = None,
        sender_id: str = "taipy",
        with_input: bool = True,
        on_action: Optional[Union[str, Callable]] = None,
        page_size: int = 50,
        height: Optional[Union[str, int, float]] = None,
        show_sender: bool = False,
        mode: str = "markdown",
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a chat element.\n\nParameters\n----------\n\nmessages (dynamic)\n  The list of messages. Each item of this list must consist of a list of three strings: a message identifier, a message content, and a user identifier.\n\nusers (dynamic)\n  The list of users. See the [section on List of Values](https://docs.taipy.io/en/release-4.0/manuals/userman/gui/viselements/generic/chat/../../../../../../userman/gui/binding/#list-of-values) for more details.\n\nsender_id\n  The user identifier, as indicated in the *users* list, associated with all messages sent from the input.\n\nwith_input (dynamic)\n  If False, the input field is not rendered.\n\non_action\n  A function or the name of a function that is triggered when the user enters a new message.  \n  This function is invoked with the following parameters:\n  \n  * *state* (`State^`): the state instance.\n  * *var_name* (str): the name of the variable bound to the *messages* property.\n  * *payload* (dict): the details on this callback's invocation.  \n    This dictionary has the following keys:\n    + *action*: the name of the action that triggered this callback.\n    + *args* (list): a list composed of a reason ("click" or "Enter"), the variable name, the message, and the user identifier of the sender.\n  \n\npage_size\n  The number of messages retrieved from the application and sent to the frontend. Larger values imply more potential latency.\n\nheight\n  The maximum height of this chat control, in CSS units.\n\nshow_sender\n  If True, the sender avatar and name are displayed.\n\nmode\n  Define the way the messages are processed when they are displayed:\n  \n  * "raw" no processing\n  * "pre": keeps spaces and new lines\n  * "markdown" or "md": basic support for Markdown.\n  \n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-chat` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class tree(_Control):
    _ELEMENT_NAME: str
    def __init__(
        self,
        expanded: Union[bool, list[str]] = True,
        *,
        multiple: bool = False,
        select_leafs_only: bool = False,
        row_height: Optional[str] = None,
        label: Optional[str] = None,
        value: Optional[Any] = None,
        on_change: Optional[Union[str, Callable]] = None,
        lov: Optional[dict[str, Any]] = None,
        adapter: Optional[Union[str, Callable]] = None,
        type: Optional[str] = None,
        value_by_id: bool = False,
        propagate: Optional[bool] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
        mode: Optional[str] = None,
        dropdown: bool = False,
        filter: bool = False,
        width: Union[str, int] = "360px",
        height: Optional[Union[str, int]] = None,
    ) -> None:
        """Creates a tree element.\n\nParameters\n----------\n\nvalue (dynamic)\n  Bound to the selection value.\n\nexpanded (dynamic)\n  If Boolean and False, only one node can be expanded at one given level. Otherwise this should be set to an array of the node identifiers that need to be expanded.\n\nmultiple\n  If True, the user can select multiple items by holding the `Ctrl` key while clicking on items.\n\nselect_leafs_only\n  If True, the user can only select leaf nodes.\n\nrow_height\n  The height of each row of this tree, in CSS units.\n\nlabel\n  The label associated with the selector when in dropdown mode.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\nlov\n  The list of values. See the [section on List of Values](https://docs.taipy.io/en/release-4.0/manuals/userman/gui/viselements/generic/tree/../../../../../../userman/gui/binding/#list-of-values) for more details.\n\nadapter\n  A function or the name of the function that transforms an element of *lov* into a *tuple(id:str, label:Union[str,Icon])*.  \n  The default value is a function that returns the string representation of the *lov* element.\n\ntype\n  This property is required if *lov* contains a non-specific type of data (e.g., a dictionary).  \n  Then:\n  \n  * *value* must be of that type\n  * *lov* must be an iterable containing elements of this type\n  * The function set to *adapter* will receive an object of this type.\n  \n    \n  The default value is the type of the first element in *lov*.\n\nvalue_by_id\n  If False, the selection value (in *value*) is the selected element in *lov*. If set to True, then *value* is set to the id of the selected element in *lov*.\n\npropagate\n  Allows the control's main value to be automatically propagated.  \n  The default value is defined at the application configuration level by the **propagate** configuration option.  \n  If True, any change to the control's value is immediately reflected in the bound application variable.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-tree` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\nmode\n  Define the way the selector is displayed:\n  \n  * "radio": as a list of radio buttons\n  * "check": as a list of check boxes\n  * any other value: a plain list.\n  \n\ndropdown\n  If True, the list of items is shown in a dropdown menu.  \n    \n  You cannot use the filter in that situation.\n\nfilter\n  If True, this control is combined with a filter input area.\n\nwidth\n  The width of this selector, in CSS units.\n\nheight\n  The height of this selector, in CSS units.\n\n"""  # noqa: E501
        ...

if find_spec("taipy.core"):
    class scenario_selector(_Control):
        _ELEMENT_NAME: str
        def __init__(
            self,
            value: Optional[Union[Scenario, list[Scenario]]] = None,
            *,
            scenarios: Optional[list[Union[Scenario, Cycle]]] = None,
            multiple: bool = False,
            filter: Union[
                bool,
                str,
                "taipy.gui_core.filters.ScenarioFilter",
                list[Union[str, "taipy.gui_core.filters.ScenarioFilter"]],
            ] = "*",
            show_search: bool = True,
            sort: Union[
                bool,
                str,
                "taipy.gui_core.filters.ScenarioFilter",
                list[Union[str, "taipy.gui_core.filters.ScenarioFilter"]],
            ] = "*",
            show_add_button: bool = True,
            display_cycles: bool = True,
            show_primary_flag: bool = True,
            show_pins: bool = False,
            on_change: Optional[Union[str, Callable]] = None,
            show_dialog: bool = True,
            on_creation: Optional[Union[str, Callable]] = None,
            height: str = "50vh",
            id: Optional[str] = None,
            class_name: Optional[str] = None,
        ) -> None:
            """Creates a scenario_selector element.\n\nParameters\n----------\n\nvalue (dynamic)\n  Bound to the selected `Scenario^`, or None if there is none.\n\nscenarios (dynamic)\n  The list of `Cycle^` or `Scenario^` objects to show.  \n  If this is None, all Cycles and Scenarios are listed.\n\nmultiple\n  If True, the user can select multiple scenarios, therefore the *value* property can hold a list of `Scenario^` objects.\n\nfilter\n  One or multiple `Scenario^` property names to filter on.  \n  If False, do not allow filter.\n\nshow_search\n  If False, prevents users from searching for scenarios by label.\n\nsort\n  A list of `Scenario^` property names to sort on.  \n  If False, do not allow sort.\n\nshow_add_button\n  If False, the button to create a new scenario is not displayed.\n\ndisplay_cycles\n  If False, the cycles are not shown.\n\nshow_primary_flag\n  If False, the primary scenarios are not identified with specific visual hint.\n\nshow_pins\n  If True, a pin is shown on each item of the selector and allows to restrict the number of displayed items.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  The parameters of that function are all optional:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (`Scenario^`): the selected scenario.\n  \n\nshow_dialog\n  If True, a dialog is shown when the user click on the 'Add scenario' button.\n\non_creation\n  A function or the name of a function that is triggered when a scenario is about to be created.  \n    \n  All the parameters of that function are optional:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of this scenario selector.\n  * payload (dict): the details on this callback's invocation.  \n    \n    This dictionary has the following keys:\n    + config (str): the name of the selected scenario configuration.\n    + date (datetime): the creation date for the new scenario.\n    + label (str): the user-specified label.\n    + properties (dict): a dictionary containing all the user-defined custom properties.\n  * The callback function can return a scenario, a string containing an error message (a scenario will not be created), or None (then a new scenario is created with the user parameters).\n  \n\nheight\n  The maximum height, in CSS units, of the control.\n\nid\n  The identifier that will be assigned to the rendered HTML component.\n\nclass_name (dynamic)\n  The list of CSS class names associated with the generated HTML Element.  \n  These class names will be added to the default `taipy_gui_core-scenario_selector`.\n\n"""  # noqa: E501
            ...

    class scenario(_Control):
        _ELEMENT_NAME: str
        def __init__(
            self,
            scenario: Optional[Union[Scenario, list[Scenario]]] = None,
            *,
            active: bool = True,
            expandable: bool = True,
            expanded: bool = True,
            show_submit: bool = True,
            show_delete: bool = True,
            show_config: bool = False,
            show_creation_date: bool = False,
            show_cycle: bool = False,
            show_tags: bool = True,
            show_properties: bool = True,
            show_sequences: bool = True,
            show_submit_sequences: bool = True,
            on_submission_change: Optional[Union[str, Callable]] = None,
            id: Optional[str] = None,
            class_name: Optional[str] = None,
        ) -> None:
            """Creates a scenario element.\n\nParameters\n----------\n\nscenario (dynamic)\n  The scenario to display and edit.  \n  If the value is a list, it must have a single element otherwise nothing is shown.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nexpandable\n  If True, the scenario viewer can be expanded.  \n  If False, the scenario viewer is not expandable and it is shown depending on expanded value.\n\nexpanded\n  If True, when a valid scenario is selected, the scenario viewer is expanded and its content is displayed.  \n  If False, the scenario viewer is collapsed and only its name and *submit* button are visible.\n\nshow_submit\n  If False, the scenario submit button is not visible.\n\nshow_delete\n  If False, the button to delete a scenario is not visible.\n\nshow_config\n  If False, the scenario configuration label is not visible.\n\nshow_creation_date\n  If False, the scenario creation date is not visible.\n\nshow_cycle\n  If False, the scenario cycle label is not visible.\n\nshow_tags\n  If False, the scenario tags are not visible.\n\nshow_properties\n  If False, the scenario properties are not visible.\n\nshow_sequences\n  If False, the scenario sequences are not visible.\n\nshow_submit_sequences\n  If False, the buttons to submit scenario sequences are not visible.\n\non_submission_change\n  A function or the name of a function that is triggered when a submission status is changed.  \n    \n  All the parameters of that function are optional:\n  \n  * state (`State^`): the state instance.\n  * submission (Submission): the submission entity containing submission information.\n  * details (dict): the details on this callback's invocation.  \n    \n    This dictionary has the following keys:\n    + submission_status (str): the new status of the submission (possible values are: "SUBMITTED", "COMPLETED", "CANCELED", "FAILED", "BLOCKED", "WAITING", or "RUNNING").\n    + job: the Job (if any) that is at the origin of the submission status change.\n    + submittable_entity (Submittable): the entity (usually a Scenario) that was submitted.\n  \n\nid\n  The identifier that will be assigned to the rendered HTML component.\n\nclass_name (dynamic)\n  The list of CSS class names associated with the generated HTML Element.  \n  These class names will be added to the default `taipy_gui_core-scenario`.\n\n"""  # noqa: E501
            ...

    class scenario_dag(_Control):
        _ELEMENT_NAME: str
        def __init__(
            self,
            scenario: Optional[Union[Scenario, list[Scenario]]] = None,
            *,
            render: bool = True,
            show_toolbar: bool = True,
            height: str = "50vh",
            width: str = "100%",
            on_action: Optional[Union[str, Callable]] = None,
            id: Optional[str] = None,
            class_name: Optional[str] = None,
        ) -> None:
            """Creates a scenario_dag element.\n\nParameters\n----------\n\nscenario (dynamic)\n  The `Scenario^` whose diagram is displayed.  \n  If the value is a list, it must have a single element otherwise nothing is shown.\n\nrender (dynamic)\n  If False, this scenario's DAG is not displayed.\n\nshow_toolbar\n  If False, the DAG toolbar is not visible.\n\nheight\n  The maximum height, in CSS units, of the control.\n\nwidth\n  The maximum width, in CSS units, of the control.\n\non_action\n  A function or the name of a function that is triggered when a a node is selected.  \n    \n  All the parameters of that function are optional:\n  \n  * state (`State^`): the state instance.\n  * entity (DataNode or Task): the entity that was selected.\n  \n\nid\n  The identifier that will be assigned to the rendered HTML component.\n\nclass_name (dynamic)\n  The list of CSS class names associated with the generated HTML Element.  \n  These class names will be added to the default `taipy_gui_core-scenario_dag`.\n\n"""  # noqa: E501
            ...

    class data_node_selector(_Control):
        _ELEMENT_NAME: str
        def __init__(
            self,
            value: Optional[Union[DataNode, list[DataNode]]] = None,
            *,
            scenario: Optional[Union[Scenario, list[Scenario]]] = None,
            datanodes: Optional[list[Union[DataNode, Scenario, Cycle]]] = None,
            multiple: bool = False,
            filter: Union[
                bool,
                str,
                "taipy.gui_core.filters.DataNodeFilter",
                list[Union[str, "taipy.gui_core.filters.DataNodeFilter"]],
            ] = "*",
            sort: Union[
                bool,
                str,
                "taipy.gui_core.filters.DataNodeFilter",
                list[Union[str, "taipy.gui_core.filters.DataNodeFilter"]],
            ] = "*",
            show_search: bool = True,
            show_pins: bool = True,
            display_cycles: bool = True,
            show_primary_flag: bool = True,
            on_change: Optional[Union[str, Callable]] = None,
            height: str = "50vh",
            id: Optional[str] = None,
            class_name: Optional[str] = None,
        ) -> None:
            """Creates a data_node_selector element.\n\nParameters\n----------\n\nvalue (dynamic)\n  Bound to the selected `DataNode^` or `DataNode^`s, or None if there is none.\n\nscenario (dynamic)\n  If set, the selector will only show the data nodes owned by this scenario or any scenario in the list.\n\ndatanodes (dynamic)\n  The list of `DataNode^`s, `Scenario^`s, or `Cycle^`s to show.  \n  All all DataNodes, Scenarios, and Cycles are shown if this is None.\n\nmultiple\n  If True, the user can select multiple data nodes, therefore the *value* property can hold a list of `DataNode^` objects.\n\nfilter\n  A list of `DataNode^` property names to filter on.  \n  If False, users cannot filter data nodes.\n\nsort\n  A list of `DataNode^` property names to sort on.  \n  If False, do not allow sort.\n\nshow_search\n  If False, prevents users from searching for data nodes by label.\n\nshow_pins\n  If True, a pin is shown on each item of the selector and allows to restrict the number of displayed items.\n\ndisplay_cycles\n  If False, the cycles are not shown in the selector.\n\nshow_primary_flag\n  If False, the primary scenarios are not identified with specific visual hint.\n\non_change\n  A function or the name of a function that is triggered when a data node is selected.  \n  The parameters of that function are all optional:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (`DataNode^`): the selected data node.\n  \n\nheight\n  The maximum height, in CSS units, of the control.\n\nid\n  The identifier that will be assigned to the rendered HTML component.\n\nclass_name (dynamic)\n  The list of CSS class names associated with the generated HTML Element.  \n  These class names will be added to the default `taipy_gui_core-data_node_selector`.\n\n"""  # noqa: E501
            ...

    class data_node(_Control):
        _ELEMENT_NAME: str
        def __init__(
            self,
            data_node: Optional[Union[DataNode, list[DataNode]]] = None,
            *,
            show_data: bool = True,
            show_properties: bool = True,
            show_history: bool = True,
            active: bool = True,
            expandable: bool = True,
            expanded: bool = True,
            show_config: bool = False,
            show_owner: bool = True,
            show_owner_label: bool = False,
            show_custom_properties: bool = True,
            show_edit_date: bool = False,
            show_expiration_date: bool = False,
            chart_config: Optional[dict] = None,
            scenario: Optional[Scenario] = None,
            id: Optional[str] = None,
            class_name: Optional[str] = None,
        ) -> None:
            """Creates a data_node element.\n\nParameters\n----------\n\ndata_node (dynamic)\n  The data node to display and edit.  \n  If the value is a list, it must have a single element otherwise nothing is shown.\n\nshow_data\n  If False, the data node value tab is not visible.\n\nshow_properties\n  If False, the data node properties tab is not visible.\n\nshow_history\n  If False, the data node history tab is not visible.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nexpandable\n  If True, the data node viewer can be expanded.  \n  If False, the data node viewer is not expandable and it is shown depending on expanded value.\n\nexpanded\n  If True, when a valid data node is selected, the data node viewer is expanded and its content is displayed.  \n  If False, the data node viewer is collapsed and only its name is visible.\n\nshow_config\n  If False, the data node configuration label is not visible.\n\nshow_owner\n  If False, the data node owner label is not visible.\n\nshow_owner_label\n  If True, the data node owner label is added to the data node label at the top of the block.\n\nshow_custom_properties\n  If False, the custom properties for this data node properties are not visible in the Properties tab.\n\nshow_edit_date\n  If False, the data node edition date is not visible.\n\nshow_expiration_date\n  If False, the data node expiration date is not visible.\n\nchart_config\n  Chart configs by data node configuration id.\n\nscenario (dynamic)\n  A variable bound to this property is set to the selected `Scenario^` when the user picks it from the list of owner scenarios accessible from the 'Owner' field in the 'Properties' tab.  \n  This property is set to None if there is no selected owner scenario.\n\nid\n  The identifier that will be assigned to the rendered HTML component.\n\nclass_name (dynamic)\n  The list of CSS class names associated with the generated HTML Element.  \n  These class names will be added to the default `taipy_gui_core-data_node`.\n\n"""  # noqa: E501
            ...

    class job_selector(_Control):
        _ELEMENT_NAME: str
        def __init__(
            self,
            value: Optional[Union[Job, list[Job]]] = None,
            *,
            show_id: bool = True,
            show_submitted_label: bool = True,
            show_submitted_id: bool = False,
            show_submission_id: bool = False,
            show_date: bool = True,
            show_cancel: bool = True,
            show_delete: bool = True,
            on_change: Optional[Union[str, Callable]] = None,
            height: str = "50vh",
            on_details: Optional[Union[str, Callable, bool]] = None,
            id: Optional[str] = None,
            class_name: Optional[str] = None,
        ) -> None:
            """Creates a job_selector element.\n\nParameters\n----------\n\nvalue (dynamic)\n  Bound to the selected `Job^`(s), or None if there is none.\n\nshow_id\n  If False, the `Job^` id is not shown in the selector.\n\nshow_submitted_label\n  If False, the `Scenario^` or `Sequence^` label is not shown in the selector.\n\nshow_submitted_id\n  If True, the `Scenario^` or `Sequence^` id is shown in the selector.\n\nshow_submission_id\n  If True, the submission id is shown in the selector.\n\nshow_date\n  If False, the `Job^` date is not shown in the selector.\n\nshow_cancel\n  If False, the Cancel buttons are not shown in the selector.\n\nshow_delete\n  If False, the Delete buttons are not shown in the selector.\n\non_change\n  A function or the name of a function that is triggered when the selection is updated.  \n  The parameters of that function are all optional:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (`Job^`): the selected job.\n  \n\nheight\n  The maximum height, in CSS units, of the control.\n\non_details\n  The name of a function that is triggered when the details icon is pressed.  \n  The parameters of that function are all optional:\n  \n  * state (`State^`): the state instance.\n  * id (str): the id of the control.\n  * payload (`dict`): a dictionary that contains the Job Id in the value for key *args*.\n  \n  If False, the icon is not shown.\n\nid\n  The identifier that will be assigned to the rendered HTML component.\n\nclass_name (dynamic)\n  The list of CSS class names associated with the generated HTML Element.  \n  These class names will be added to the default `taipy_gui_core-job_selector`.\n\n"""  # noqa: E501
            ...

class part(_Block):
    _ELEMENT_NAME: str
    def __init__(
        self,
        render: bool = True,
        *,
        class_name: Optional[str] = None,
        page: Optional[str] = None,
        height: Optional[str] = None,
        content: Optional[Any] = None,
        partial: Optional["taipy.gui.Partial"] = None,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a part element.\n\nParameters\n----------\n\nclass_name (dynamic)\n  A list of CSS class names, separated by white spaces, that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-part` class name.\n\nrender (dynamic)\n  If True, this part is visible on the page.  \n  If False, the part is hidden and its content is not displayed.\n\npage (dynamic)\n  The page to show as the content of the block (page name if defined or a URL in an *iframe*).  \n  This should not be defined if *partial* is set.\n\nheight (dynamic)\n  The height, in CSS units, of this block.\n\ncontent (dynamic)\n  The content provided to the part. See the documentation section on content providers.\n\npartial\n  A Partial object that holds the content of the block.  \n  This should not be defined if *page* is set.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class expandable(_Block):
    _ELEMENT_NAME: str
    def __init__(
        self,
        title: Optional[str] = None,
        *,
        expanded: bool = True,
        page: Optional[str] = None,
        partial: Optional["taipy.gui.Partial"] = None,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
        on_change: Optional[Union[str, Callable]] = None,
    ) -> None:
        """Creates an expandable element.\n\nParameters\n----------\n\ntitle (dynamic)\n  Title of this block element.\n\nexpanded (dynamic)\n  If True, the block is expanded, and the content is displayed.  \n  If False, the block is collapsed and its content is hidden.\n\npage\n  The page name to show as the content of the block.  \n  This should not be defined if *partial* is set.\n\npartial\n  A Partial object that holds the content of the block.  \n  This should not be defined if *page* is set.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-expandable` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\n"""  # noqa: E501
        ...

class dialog(_Block):
    _ELEMENT_NAME: str
    def __init__(
        self,
        open: bool = False,
        *,
        on_action: Optional[Union[str, Callable]] = None,
        close_label: str = "Close",
        labels: Optional[Union[str, list[str]]] = None,
        width: Optional[Union[str, int, float]] = None,
        height: Optional[Union[str, int, float]] = None,
        page: Optional[str] = None,
        partial: Optional["taipy.gui.Partial"] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a dialog element.\n\nParameters\n----------\n\nopen\n  If True, the dialog is visible. If False, it is hidden.\n\non_action\n  A function or the name of a function triggered when a button is pressed.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (str): the identifier of the dialog if it has one.\n  * payload (dict): the details on this callback's invocation.  \n    This dictionary has the following keys:\n    + action: the name of the action that triggered this callback.\n    + args: a list where the first element contains the index of the selected label.\n  \n\nclose_label\n  The tooltip of the top-right close icon button. In the `on_action` callback, *args* will be set to -1.\n\nlabels\n  A list of labels to show in a row of buttons at the bottom of the dialog. The index of the button in the list is reported as args in the `on_action` callback (that index is -1 for the *close* icon).\n\nwidth\n  The width of this dialog, in CSS units.\n\nheight\n  The height of this dialog, in CSS units.\n\npage\n  The page name to show as the content of the block.  \n  This should not be defined if *partial* is set.\n\npartial\n  A Partial object that holds the content of the block.  \n  This should not be defined if *page* is set.\n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-dialog` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class layout(_Block):
    _ELEMENT_NAME: str
    def __init__(
        self,
        columns: str = "1 1",
        *,
        columns__mobile: str = "1",
        gap: str = "0.5rem",
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a layout element.\n\nParameters\n----------\n\ncolumns\n  The list of weights for each column.  \n  For example, "1 2" creates a 2 column grid:\n  \n  * 1fr\n  * 2fr\n  \n    \n  The creation of multiple same size columns can be simplified by using the multiply sign eg. "5*1" is equivalent to "1 1 1 1 1".\n\ncolumns[mobile]\n  The list of weights for each column, when displayed on a mobile device.  \n  The syntax is the same as for *columns*.\n\ngap\n  The size of the gap between the columns.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-layout` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...

class pane(_Block):
    _ELEMENT_NAME: str
    def __init__(
        self,
        open: bool = False,
        *,
        on_close: Optional[Union[str, Callable]] = None,
        anchor: str = "left",
        persistent: bool = False,
        width: str = "30vw",
        height: str = "30vh",
        show_button: bool = False,
        page: Optional[str] = None,
        partial: Optional["taipy.gui.Partial"] = None,
        on_change: Optional[Union[str, Callable]] = None,
        active: bool = True,
        id: Optional[str] = None,
        properties: Optional[dict[str, Any]] = None,
        class_name: Optional[str] = None,
        hover_text: Optional[str] = None,
    ) -> None:
        """Creates a pane element.\n\nParameters\n----------\n\nopen (dynamic)\n  If True, this pane is visible on the page.  \n  If False, the pane is hidden.\n\non_close\n  A function or the name of a function that is triggered when this pane is closed (if the user clicks outside of it or presses the Esc key).  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * id (optional[str]): the identifier of the *close* button if it has one.\n  \n    \n  If this property is not set, no function is called when this pane is closed.\n\nanchor\n  Anchor side of the pane.  \n  Valid values are "left", "right", "top", or "bottom".\n\npersistent\n  If False, the pane covers the page where it appeared and disappears if the user clicks in the page.  \n  If True, the pane appears next to the page. Note that the parent section of the pane must have the *flex* display mode set.\n\nwidth\n  Width, in CSS units, of this pane.  \n  This is used only if *anchor* is "left" or "right".\n\nheight\n  Height, in CSS units, of this pane.  \n  This is used only if *anchor* is "top" or "bottom".\n\nshow_button\n  If True and when the pane is closed, a button allowing the pane to be opened is shown.\n\npage\n  The page name to show as the content of the block.  \n  This should not be defined if *partial* is set.\n\npartial\n  A Partial object that holds the content of the block.  \n  This should not be defined if *page* is set.\n\non_change\n  A function or the name of a function that is triggered when the value is updated.  \n  This function is invoked with the following parameters:\n  \n  * state (`State^`): the state instance.\n  * var_name (str): the variable name.\n  * value (Any): the new value.\n  \n\nactive (dynamic)\n  Indicates if this component is active.  \n  An inactive component allows no user interaction.\n\nid\n  The identifier that is assigned to the rendered HTML component.\n\nproperties\n  Bound to a dictionary that contains additional properties for this element.\n\nclass_name (dynamic)\n  The list of CSS class names that are associated with the generated HTML Element.  \n  These class names are added to the default `taipy-pane` class name.\n\nhover_text (dynamic)\n  The information that is displayed when the user hovers over this element.\n\n"""  # noqa: E501
        ...
