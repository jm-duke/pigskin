import pytest
import requests

from pigskin.pigskin import pigskin
from pigskin.pigskin import settings

gp = pigskin()


@pytest.mark.vcr()
def test_invalid_response_get_bytes():
    junk_url = 'https://httpbin.org/bytes/20'
    diva_config_url = gp._store.gp_config['modules']['DIVA']['HTML5']['SETTINGS']['Live24x7']
    gp._store.gp_config['modules']['API'] = { key: junk_url for key in gp._store.gp_config['modules']['API'] }
    gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] }
    gp.gigya_auth_url = junk_url

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')
    assert not gp.get_nfl_network_streams()
    assert not gp.get_redzone_streams()
    assert not gp._get_diva_config(junk_url)
    assert not gp._get_diva_streams(video_id='invalid', diva_config_url=diva_config_url)
    assert not gp.check_for_subscription()
    assert gp.is_redzone_on_air() == None


@pytest.mark.vcr()
def test_invalid_response_get_html():
    junk_url = 'https://httpbin.org/html'
    diva_config_url = gp._store.gp_config['modules']['DIVA']['HTML5']['SETTINGS']['Live24x7']
    gp._store.gp_config['modules']['API'] = { key: junk_url for key in gp._store.gp_config['modules']['API'] }
    gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] }
    gp.gigya_auth_url = junk_url

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')
    assert not gp.get_nfl_network_streams()
    assert not gp.get_redzone_streams()
    assert not gp._get_diva_config(junk_url)
    assert not gp._get_diva_streams(video_id='invalid', diva_config_url=diva_config_url)
    assert not gp.check_for_subscription()
    assert gp.is_redzone_on_air() == None


@pytest.mark.vcr()
def test_invalid_response_get_json():
    junk_url = 'https://httpbin.org/json'
    diva_config_url = gp._store.gp_config['modules']['DIVA']['HTML5']['SETTINGS']['Live24x7']
    gp._store.gp_config['modules']['API'] = { key: junk_url for key in gp._store.gp_config['modules']['API'] }
    gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] }
    gp.gigya_auth_url = junk_url

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')
    assert not gp.get_nfl_network_streams()
    assert not gp.get_redzone_streams()
    assert not gp._get_diva_config(junk_url)
    assert not gp._get_diva_streams(video_id='invalid', diva_config_url=diva_config_url)
    assert not gp.check_for_subscription()
    assert gp.is_redzone_on_air() == None


@pytest.mark.vcr()
def test_invalid_response_get_xml():
    junk_url = 'https://httpbin.org/xml'
    diva_config_url = gp._store.gp_config['modules']['DIVA']['HTML5']['SETTINGS']['Live24x7']
    gp._store.gp_config['modules']['API'] = { key: junk_url for key in gp._store.gp_config['modules']['API'] }
    gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] }
    gp.gigya_auth_url = junk_url

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')
    assert not gp.get_nfl_network_streams()
    assert not gp.get_redzone_streams()
    assert not gp._get_diva_config(junk_url)
    assert not gp._get_diva_streams(video_id='invalid', diva_config_url=diva_config_url)
    assert not gp.check_for_subscription()
    assert gp.is_redzone_on_air() == None


@pytest.mark.vcr()
def test_invalid_response_post_json():
    junk_url = 'https://httpbin.org/post'
    diva_config_url = gp._store.gp_config['modules']['DIVA']['HTML5']['SETTINGS']['Live24x7']
    gp._store.gp_config['modules']['API'] = { key: junk_url for key in gp._store.gp_config['modules']['API'] }
    gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp._store.gp_config['modules']['ROUTES_DATA_PROVIDERS'] }

    gigya_auth_url_original = settings.gigya_auth_url
    settings.gigya_auth_url = junk_url

    # it seems that httbin only provides JSON responses to POST requests
    # TODO: find a way to get html and bytes responses for POST as well
    assert not gp.login(username='nope', password='so_secret', force=True)
    assert not gp._gigya_auth(username='nope', password='so_secret')
    assert not gp._gp_auth(username='nope', password='so_secret')
    assert not gp.refresh_tokens()

    # restore the setting
    settings.gigya_auth_url = gigya_auth_url_original
