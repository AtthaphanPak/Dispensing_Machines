def  load_operation_list(operation_raw: str):
    return [op.strip() for op in operation_raw.split(",") if op.strip()]

def is_valid_en(en: str):
    return len(en) == 6 and en.isnumeric()

def is_valid_serial(serial: str):
    return len(serial) == 12

