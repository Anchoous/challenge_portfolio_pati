from pages.base_page import BasePage


class Dashboard(BasePage):
    header_logo_scouts_panel = "//header/div/h6"
    main_page_button = "//*[@class = 'jss50']//span"
    players_button = "//div/ul/div[2]/div[2]/span"
    change_language_button = "//ul[2]/div[1]/div[1]"
    sing_out_button = "//ul[2]/div[2]/div[2]/span"
    players_count_box = "//main/div[2]/div[1]/div"
    reports_count_box = "//main/div[2]/div[3]/div"
    events_count_box = "main/div[2]/div[4]/div"
    add_player_button = "//a[contains(@href, 'add')]/button"
    dev_team_contact_button = "//a[contains(@href, 'slack')]"
