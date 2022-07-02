class ErrorMessage():
    required = "必須項目です"
    null = "必須項目です"
    blank = "1文字以上で入力してください"
    max_length = "最大文字数以下で入力してください"
    min_length = "最小文字数以上で入力してください"

    def __set_field_name(self, field_name) -> None:
        self.required = f"{field_name}は{self.required}"
        self.null = f"{field_name}は{self.null}"
        self.blank = f"{field_name}は{self.blank}"
        self.max_length = f"{field_name}は{self.max_length}"
        self.min_length = f"{field_name}は{self.min_length}"

    def __init__(self, field_name=None, max_length=None, min_length=None) -> None:
        if field_name is not None: self.__set_field_name(field_name=field_name)
        if max_length is not None: self.max_length = f"{max_length}文字以下で入力してください"
        if min_length is not None: self.min_length = f"{min_length}文字以上で入力してください"

    def __str__(self) -> str:
        print("required:", self.required)
        print("null:", self.null)
        print("blank:", self.blank)
        print("max_length:", self.max_length)
        print("min_length:", self.min_length)

    def get_error_messages(self) -> dict:
        return {
            "required": self.required,
            "null": self.null,
            "blank": self.blank,
            "max_length": self.max_length,
            "min_length": self.min_length
        }