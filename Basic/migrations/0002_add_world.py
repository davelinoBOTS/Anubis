from django.db import migrations


def load_list_country_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_country.sql'), 'r', encoding="utf8").read()

    return sql_statements


def delete_list_country_with_sql():
    return 'DELETE from "Basic_country";'


def load_add_list_state_brasil_centro_oeste_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_state_brasil_centro_oeste.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def load_add_list_state_brasil_nordeste_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_state_brasil_nordeste.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def load_add_list_state_brasil_norte_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_state_brasil_norte.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def load_add_list_state_brasil_sudeste_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_state_brasil_sudeste.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def load_add_list_state_brasil_sul_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_state_brasil_sul.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def delete_list_state_with_sql():
    return 'DELETE from "Basic_state";'


def load_add_list_territory_brasil_nordeste_piaui_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_territory_brasil_nordeste_piaui.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def delete_list_territory_with_sql():
    return 'DELETE from "Basic_territory";'


def load_add_list_city_brasil_nordeste_piaui_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_city_brasil_nordeste_piaui.sql'), 'r',
                          encoding="utf8").read()

    return sql_statements


def delete_list_city_with_sql():
    return 'DELETE from "Basic_city";'


def load_add_list_neighborhood_brasil_nordeste_piaui_teresina_from_sql():
    from Anubis.settings import BASE_DIR
    import os

    sql_statements = open(os.path.join(BASE_DIR, 'Basic/sql/add_list_neighborhood_brasil_nordeste_piaui_teresina.sql'),
                          'r',  encoding="utf8").read()

    return sql_statements


def delete_list_neighborhood_with_sql():
    return 'DELETE from "Basic_neighborhood";'


class Migration(migrations.Migration):
    dependencies = [
        ('Basic', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(load_list_country_from_sql(),
                          delete_list_country_with_sql()),
        migrations.RunSQL(load_add_list_state_brasil_centro_oeste_from_sql(),
                          delete_list_state_with_sql()),
        migrations.RunSQL(load_add_list_state_brasil_nordeste_from_sql(),
                          delete_list_state_with_sql()),
        migrations.RunSQL(load_add_list_state_brasil_norte_from_sql(),
                          delete_list_state_with_sql()),
        migrations.RunSQL(load_add_list_state_brasil_sudeste_from_sql(),
                          delete_list_state_with_sql()),
        migrations.RunSQL(load_add_list_state_brasil_sul_from_sql(),
                          delete_list_state_with_sql()),
        migrations.RunSQL(load_add_list_territory_brasil_nordeste_piaui_from_sql(),
                          delete_list_territory_with_sql()),
        migrations.RunSQL(load_add_list_city_brasil_nordeste_piaui_from_sql(),
                          delete_list_city_with_sql()),
        migrations.RunSQL(load_add_list_neighborhood_brasil_nordeste_piaui_teresina_from_sql(),
                          delete_list_neighborhood_with_sql())
    ]
