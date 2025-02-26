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
    WAIT_APP_START = 2


@unique
class XmlIdEnum(str, Enum):
    SEARCH_VIEW_CONTAINER = "com.avito.android:id/search_view_container"
    TOOLBAR_CONTAINER = "com.avito.android:id/toolbar_container"
    CONTAINER = "com.avito.android:id/container"
    INPUT_VIEW = "com.avito.android:id/input_view"
    SUGGESTS_RECYCLER_VIEW = "com.avito.android:id/suggests_recycler_view"
    SEARCH_VIEW_ITEM = "com.avito.android:id/search_view_item"
    ICON_CONTAINER = "com.avito.android:id/icon_container"
    FILTERS_TEXT = "com.avito.android:id/filters_text"
    CONTENT = "android:id/content"
    FILTERS_SCREEN_ROOT = "com.avito.android:id/filters_screen_root"
    DESIGN_ITEM_TITLE = "com.avito.android:id/design_item_title"
    TEXT_VIEW = "com.avito.android:id/text_view"
    RECYCLER_VIEW = "com.avito.android:id/recycler_view"
    MENU_SHARE = "com.avito.android:id/menu_share"
    SUGGEST_TITLE = "com.avito.android:id/suggest_title"
    MAIN_TEXT = "com.avito.android:id/mainText"


@unique
class XmlClassEnum(str, Enum):
    TEXT_VIEW = "android.widget.TextView"
    LINEAR_LAYOUT = "android.widget.LinearLayout"
    FRAME_LAYOUT = "android.widget.FrameLayout"
    RECYCLER_VIEW = "androidx.recyclerview.widget.RecyclerView"
    BUTTON = "android.widget.Button"
    EDIT_TEXT = "android.widget.EditText"


@unique
class StrEnum(str, Enum):
    UTF = "utf-8"

    # file names
    FIRST_SCREEN = "first_screen.xml"
    SECOND_SCREEN = "second_screen.xml"
    RESULT_TXT = "links.txt"

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
    URL_APP = "com.example.app"
    SEARCH_TEXT = "littlest pet shop"
    TARGET = r"littlest pet shop|lps|лпс|стоячки|Littlest Pet Shop|lps стоячка|Littlest pet shop|Littlest Pet shop|"
    
