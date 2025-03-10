from enum import StrEnum, unique

@unique
class TextEnum(StrEnum):
    MAIN_TEXT = "Avito Andriod Parser"
    HELPER_TEX_TFIELD = "For submit press button 'Submit'"
    TEXT_CHAT_ID = "Telegram chat id :"
    TEXT_PHONE_ID = "Phone serial number :"
    TEXT_SEARCH_QUERY = "Search query :"
    BTN_SUBMIT = "Submit"
    BTN_START = "Start"
    BTN_STOP = "Stop"
