class dotdict(dict):
    """
    . 연산자로 사전형 데이터 속성값 접근, 수정 가능
    재귀적으로 dict 데이터를 dotdict으로 변환
    usage:
    d = dotdict({"a": 1, "b": {"c": 2, "d": 3}})
    ## GET
    > print(d.a)  # 1
    > print(d.b.c)  # 2
    ## SET
    > d.b.d = 5
    > print(d.b.d)  # 5
    """

    __setattr__ = dict.__setitem__  # type: ignore

    def __init__(self, dct={}):
        for key in dct.keys():
            value = dct[key]

            # value 값이 dict인지 체크
            if hasattr(value, "keys"):
                value = dotdict(value)

            # 리스트 타입일 경우 리스트 내 객체들이 dict인지 체크
            if isinstance(value, list):
                temp = []
                for data in value:
                    if hasattr(data, "keys"):
                        data = dotdict(data)
                    temp.append(data)
                value = temp

            self[key] = value

    def __getattr__(self, name: str):
        try:
            return self[name]
        except KeyError as e:
            raise KeyError(f"해당 키({name})는 존재하지 않습니다.") from e

    def __delattr__(self, name: str) -> None:
        try:
            del self[name]
        except KeyError as e:
            raise KeyError(f"해당 키({name})는 존재하지 않습니다. 삭제에 실패했습니다.") from e


if __name__ == "__main__":
    d = dotdict({"a": 1, "b": {"c": 2, "d": 3}, "e": [1, 2, 3, {"f": 4}]})
    print(d.a)
    print(d.b.c)
    print(d.e[3].f)
