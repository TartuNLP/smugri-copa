from functools import partial


def convert_choice(choice):
    return choice[0].lower() + choice[1:]


def doc_to_text(doc, connector):
    # Drop the period
    conn = connector[doc["question"]]
    punct = connector.get("punctuation", "")
    return doc["premise"].strip()[:-1] + f"{punct} {conn}"


def doc_to_choice(doc):
    return [convert_choice(doc["choice1"]), convert_choice(doc["choice2"])]


CONNECTORS = {
    "eng_Latn": {
        "cause": "because",
        "effect": "therefore",
        "punctuation": ",",
    },
    "est_Latn": {
        "cause": "sest",
        "effect": "seetõttu",
        "punctuation": ",",
    },
    "vro_Latn": {
        "cause": "selle et",
        "effect": "tuuperäst",
        "punctuation": ",",
    },
    "liv_Latn": {
        "cause": "sīest",
        "effect": "sīepierāst",
        "punctuation": ",",
    }
}

doc_to_text_est_Latn = partial(
    doc_to_text,
    connector=CONNECTORS["est_Latn"]
)

doc_to_text_vro_Latn = partial(
    doc_to_text,
    connector=CONNECTORS["vro_Latn"]
)

doc_to_text_liv_Latn = partial(
    doc_to_text,
    connector=CONNECTORS["liv_Latn"]
)