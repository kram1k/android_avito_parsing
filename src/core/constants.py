from enum import Enum, unique


@unique
class FloatEnum(float, Enum):
    DELAY_WIDGET = 25.0
    DELAY_SCREEN = 30.0


@unique
class IntEnum(int, Enum):
    TIME_TO_SCROLL = 10
    WAIT_SCROLL_DONE = 5
    COUNT_SCROLLS = 3


@unique
class StrEnum(str, Enum):
    UTF = "utf-8"

    # resourceId
    ID_SEARCH_VIEW_CONTAINER = "com.avito.android:id/search_view_container"
    ID_TOOLBAR_CONTAINER = "com.avito.android:id/toolbar_container"
    ID_CONTAINER = "com.avito.android:id/container"
    ID_INPUT_VIEW = "com.avito.android:id/input_view"
    ID_SUGGESTS_RECYCLER_VIEW = "com.avito.android:id/suggests_recycler_view"
    ID_SEARCH_VIEW_ITEM = "com.avito.android:id/search_view_item"
    ID_ICON_CONTAINER = "com.avito.android:id/icon_container"
    ID_FILTERS_TEXT = "com.avito.android:id/filters_text"
    ID_CONTENT = "android:id/content"
    ID_FILTERS_SCREEN_ROOT = "com.avito.android:id/filters_screen_root"
    ID_DESIGN_ITEM_TITLE = "com.avito.android:id/design_item_title"
    ID_TEXT_VIEW = "com.avito.android:id/text_view"
    ID_RECYCLER_VIEW_ID = "com.avito.android:id/recycler_view"
    ID_MENU_SHARE_ID = "com.avito.android:id/menu_share"
    ID_SUGGEST_TITLE = "com.avito.android:id/suggest_title"

    # className
    CLASS_TEXT_VIEW = "android.widget.TextView"
    CLASS_LINEAR_LAYOUT = "android.widget.LinearLayout"
    CLASS_FRAME_LAYOUT = "android.widget.FrameLayout"
    CLASS_RECYCLER_VIEW_CLASS = "androidx.recyclerview.widget.RecyclerView"
    CLASS_BUTTON_CLASS = "android.widget.Button"
    CLASS_EDIT_TEXT = "android.widget.EditText"

    # screen name constants
    FIRST_SCREEN = "first_screen.xml"
    SECOND_SCREEN = "second_screen.xml"

    # constants for parse xml files
    TEXT = "text"
    NODE = "node"

    # ru Develop constants
    RU_SEARCH_TEXT = "Поиск во всех регионах"
    FILTER_BUTTON = "Фильтры"
    TO_DATE = "По дате"
    ACCEPT_BUTTON = "Показать больше 1 тыс. объявлений"

    # en Develop constants
    AVITO = "com.avito.android"
    SEARCH_TEXT = "littlest pet shop"
