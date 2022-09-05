import os

from iso639 import languages

from promptsource.templates import Template, TemplateCollection


_LanguagePairs = [
    ("afr", "eng"),
    ("afr", "som"),
    ("amh", "eng"),
    ("amh", "fra"),
    ("amh", "nya"),
    ("amh", "orm"),
    ("amh", "sna"),
    ("amh", "som"),
    ("amh", "ssw"),
    ("amh", "swh"),
    ("amh", "tsn"),
    ("amh", "tso"),
    ("amh", "umb"),
    ("amh", "xho"),
    ("amh", "yor"),
    ("amh", "zul"),
    ("eng", "fuv"),
    ("eng", "hau"),
    ("eng", "ibo"),
    ("eng", "kam"),
    ("eng", "kin"),
    ("eng", "lin"),
    ("eng", "lug"),
    ("eng", "luo"),
    ("eng", "nso"),
    ("eng", "nya"),
    ("eng", "orm"),
    ("eng", "sna"),
    ("eng", "som"),
    ("eng", "ssw"),
    ("eng", "swh"),
    ("eng", "tsn"),
    ("eng", "tso"),
    ("eng", "umb"),
    ("eng", "wol"),
    ("eng", "xho"),
    ("eng", "yor"),
    ("eng", "zul"),
    ("fra", "hau"),
    ("fra", "ibo"),
    ("fra", "kam"),
    ("fra", "kin"),
    ("fra", "lin"),
    ("fra", "lug"),
    ("fra", "luo"),
    ("fra", "nso"),
    ("fra", "nya"),
    ("fra", "orm"),
    ("fra", "som"),
    ("fra", "ssw"),
    ("fra", "swh"),
    ("fra", "tsn"),
    ("fra", "tso"),
    ("fra", "umb"),
    ("fra", "wol"),
    ("fra", "xho"),
    ("fra", "zul"),
    ("fuv", "hau"),
    ("fuv", "ibo"),
    ("fuv", "kam"),
    ("fuv", "kin"),
    ("fuv", "lug"),
    ("fuv", "luo"),
    ("fuv", "nso"),
    ("fuv", "nya"),
    ("fuv", "orm"),
    ("fuv", "sna"),
    ("fuv", "som"),
    ("fuv", "ssw"),
    ("fuv", "swh"),
    ("fuv", "tsn"),
    ("fuv", "tso"),
    ("fuv", "umb"),
    ("fuv", "xho"),
    ("fuv", "yor"),
    ("fuv", "zul"),
    ("hau", "ibo"),
    ("hau", "kam"),
    ("hau", "kin"),
    ("hau", "lug"),
    ("hau", "luo"),
    ("hau", "nso"),
    ("hau", "nya"),
    ("hau", "orm"),
    ("hau", "sna"),
    ("hau", "som"),
    ("hau", "ssw"),
    ("hau", "swh"),
    ("hau", "tsn"),
    ("hau", "tso"),
    ("hau", "umb"),
    ("hau", "xho"),
    ("hau", "yor"),
    ("hau", "zul"),
    ("ibo", "kam"),
    ("ibo", "kin"),
    ("ibo", "lug"),
    ("ibo", "luo"),
    ("ibo", "nso"),
    ("ibo", "nya"),
    ("ibo", "orm"),
    ("ibo", "sna"),
    ("ibo", "som"),
    ("ibo", "ssw"),
    ("ibo", "swh"),
    ("ibo", "tsn"),
    ("ibo", "tso"),
    ("ibo", "umb"),
    ("ibo", "xho"),
    ("ibo", "yor"),
    ("ibo", "zul"),
    ("kam", "kin"),
    ("kam", "lug"),
    ("kam", "luo"),
    ("kam", "nso"),
    ("kam", "nya"),
    ("kam", "orm"),
    ("kam", "sna"),
    ("kam", "som"),
    ("kam", "ssw"),
    ("kam", "swh"),
    ("kam", "tsn"),
    ("kam", "tso"),
    ("kam", "umb"),
    ("kam", "xho"),
    ("kam", "yor"),
    ("kam", "zul"),
    ("kin", "lug"),
    ("kin", "luo"),
    ("kin", "nso"),
    ("kin", "nya"),
    ("kin", "orm"),
    ("kin", "sna"),
    ("kin", "som"),
    ("kin", "ssw"),
    ("kin", "swh"),
    ("kin", "tsn"),
    ("kin", "tso"),
    ("kin", "umb"),
    ("kin", "xho"),
    ("kin", "yor"),
    ("kin", "zul"),
    ("lug", "luo"),
    ("lug", "nso"),
    ("lug", "nya"),
    ("lug", "orm"),
    ("lug", "sna"),
    ("lug", "som"),
    ("lug", "ssw"),
    ("lug", "swh"),
    ("lug", "tsn"),
    ("lug", "tso"),
    ("lug", "umb"),
    ("lug", "xho"),
    ("lug", "yor"),
    ("lug", "zul"),
    ("luo", "nso"),
    ("luo", "nya"),
    ("luo", "orm"),
    ("luo", "sna"),
    ("luo", "som"),
    ("luo", "ssw"),
    ("luo", "swh"),
    ("luo", "tsn"),
    ("luo", "tso"),
    ("luo", "umb"),
    ("luo", "xho"),
    ("luo", "yor"),
    ("luo", "zul"),
    ("nso", "nya"),
    ("nso", "orm"),
    ("nso", "sna"),
    ("nso", "som"),
    ("nso", "ssw"),
    ("nso", "swh"),
    ("nso", "tsn"),
    ("nso", "tso"),
    ("nso", "umb"),
    ("nso", "xho"),
    ("nso", "yor"),
    ("nso", "zul"),
    ("nya", "orm"),
    ("nya", "sna"),
    ("nya", "som"),
    ("nya", "ssw"),
    ("nya", "swh"),
    ("nya", "tsn"),
    ("nya", "tso"),
    ("nya", "umb"),
    ("nya", "xho"),
    ("nya", "yor"),
    ("nya", "zul"),
    ("orm", "sna"),
    ("orm", "som"),
    ("orm", "ssw"),
    ("orm", "swh"),
    ("orm", "tsn"),
    ("orm", "tso"),
    ("orm", "umb"),
    ("orm", "xho"),
    ("orm", "yor"),
    ("orm", "zul"),
    ("sna", "som"),
    ("sna", "ssw"),
    ("sna", "swh"),
    ("sna", "tsn"),
    ("sna", "tso"),
    ("sna", "umb"),
    ("sna", "xho"),
    ("sna", "yor"),
    ("sna", "zul"),
    ("som", "ssw"),
    ("som", "swh"),
    ("som", "tsn"),
    ("som", "tso"),
    ("som", "umb"),
    ("som", "wol"),
    ("som", "xho"),
    ("som", "yor"),
    ("som", "zul"),
    ("ssw", "swh"),
    ("ssw", "tsn"),
    ("ssw", "tso"),
    ("ssw", "umb"),
    ("ssw", "xho"),
    ("ssw", "yor"),
    ("ssw", "zul"),
    ("swh", "tsn"),
    ("swh", "tso"),
    ("swh", "umb"),
    ("swh", "xho"),
    ("swh", "yor"),
    ("swh", "zul"),
    ("tsn", "tso"),
    ("tsn", "umb"),
    ("tsn", "xho"),
    ("tsn", "yor"),
    ("tsn", "zul"),
    ("tso", "umb"),
    ("tso", "xho"),
    ("tso", "yor"),
    ("tso", "zul"),
    ("umb", "xho"),
    ("umb", "yor"),
    ("umb", "zul"),
    ("xho", "yor"),
    ("xho", "zul"),
    ("yor", "zul"),
]

BLOOM_LANGS = """
- ak
- ar
- as
- bm
- bn
- ca
- code
- en
- es
- eu
- fon
- fr
- gu
- hi
- id
- ig
- ki
- kn
- lg
- ln
- ml
- mr
- ne
- nso
- ny
- or
- pa
- pt
- rn
- rw
- sn
- st
- sw
- ta
- te
- tn
- ts
- tum
- tw
- ur
- vi
- wo
- xh
- yo
- zh
- zu
"""

bloom_lang_codes = []
for lang in BLOOM_LANGS.split("\n")[1:-1]:
    iso2 = lang.replace("- ", "")
    bloom_lang_codes.append(iso2)
    try:
        name = languages.get(alpha2=iso2)
        bloom_lang_codes.append(name.name.lower())
        # name is e.g. 'swahili (macrolanguage)' also add swahili
        bloom_lang_codes.append(name.name.lower().split(" ")[0])
        iso3 = name.part3
        bloom_lang_codes.append(iso3)
    except KeyError:
        print(f"Could not find code {iso2}. Skipping...")
        continue

# Discrepencies
bloom_lang_codes.append("cmn")  # == zho
bloom_lang_codes.append("npi")  # == npe
bloom_lang_codes.append("ory")  # == ori
bloom_lang_codes.append("swh")  # == swa


SAME_PROMPT = (
    """Text in {}: {{{{translation["{}"] }}}}\nTranslation of the previous text to {}: ||| {{{{translation["{}"]}}}}"""
)

for lang_pair in _LanguagePairs:

    l1_code, l2_code = lang_pair

    if l1_code not in bloom_lang_codes or l2_code not in bloom_lang_codes:
        print(f"Skipping as {l1_code} or {l2_code} was not pre-trained on.")
        continue
    elif l1_code == l2_code:
        continue
    elif os.path.exists(
        f"/Users/niklasmuennighoff/Desktop/promptsource/promptsource/templates/allenai/wmt22_african/{'-'.join(lang_pair)}"
    ):
        print("Exists")
        continue

    template_collection = TemplateCollection()
    target_templates = template_collection.get_dataset("allenai/wmt22_african", "-".join(lang_pair))
    try:
        l1_name = languages.get(part3=l1_code.split("_")[0]).name
        l2_name = languages.get(part3=l2_code.split("_")[0]).name
    except KeyError:
        print(f"Could not find name {l1_code} or {l2_code}. Skipping..")
        continue

    template_name = "text-translation-" + l1_code + "-" + l2_code
    jinja = SAME_PROMPT.format(l1_name, l1_code, l2_name, l2_code)
    target_template = Template(template_name, jinja, "")
    target_templates.add_template(target_template)

    template_name = "text-translation-" + l2_code + "-" + l1_code
    jinja = SAME_PROMPT.format(l2_name, l2_code, l1_name, l1_code)
    target_template = Template(template_name, jinja, "")
    target_templates.add_template(target_template)
