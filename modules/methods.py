#
# * cmd_content = текст голосовой команды
# * alias_content = имена голосового помощника
# * return data = Всё что идёт после голосовой команды
def alias_replacer(alias_names_list, cmd_content_list, data):
    for name in alias_names_list:
        if name in data:
            data.remove(name)

    for item in data:
        for config_items in cmd_content_list:
            config_items = config_items.split()
            for config_item in config_items:
                if config_item in data:
                    data.remove(config_item)
    return data
