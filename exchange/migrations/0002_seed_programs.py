"""Крок 1. Дані з таблиці деканату переносяться рівно як є (RunSQL), нічого не виправляємо."""
from django.db import migrations

TABLE = "exchange_exchangeprogram"

FORWARD = [
    f"INSERT INTO {TABLE} (university, languages, seats, deadline, description) VALUES "
    "('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', "
    "'Давній партнер ФГН: з Варшавським університетом кафедри співпрацюють, зокрема, у спільній магістерській програмі Східноєвропейські студії.');",

    f"INSERT INTO {TABLE} (university, languages, seats, deadline, description) VALUES "
    "('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', "
    "'Один з найстаріших університетів Європи з сильними гуманітарними програмами та широким вибором курсів англійською.');",

    f"INSERT INTO {TABLE} (university, languages, seats, deadline, description) VALUES "
    "('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', "
    "'Найстаріший університет Литви з англомовними курсами з історії, філософії та культурних студій.');",

    f"INSERT INTO {TABLE} (university, languages, seats, deadline, description) VALUES "
    "('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', "
    "'Краківський університет, заснований 1364 року, партнер ФГН в історії, філології та юдаїці.');",

    f"INSERT INTO {TABLE} (university, languages, seats, deadline, description) VALUES "
    "('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', "
    "'Провідний університет Естонії, відомий гуманітарними й семіотичними студіями та курсами англійською.');",

    f"INSERT INTO {TABLE} (university, languages, seats, deadline, description) VALUES "
    "('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', "
    "'Університет у Брно з сильними факультетами філософії та мистецтв і англомовними курсами.');",
]

# До моменту відкату цієї міграції міграції 0003/0004 вже відкочені, але рядок university
# відновлюється у вигляді "Назва, Країна", а не в оригінальному, тому шукаємо за початком назви.
BACKWARD = [
    f"DELETE FROM {TABLE} WHERE "
    "university LIKE 'Uniwersytet Warszawski%' OR university LIKE 'KU Leuven%' "
    "OR university LIKE 'Vilnius University%' OR university LIKE 'Uniwersytet Jagiello%' "
    "OR university LIKE 'University of Tartu%' OR university LIKE 'Masaryk University%';"
]


class Migration(migrations.Migration):
    dependencies = [("exchange", "0001_initial")]
    operations = [migrations.RunSQL(sql=FORWARD, reverse_sql=BACKWARD)]
