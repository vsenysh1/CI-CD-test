import pytest
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.e2e


def test_calculator_adds_two_numbers(page: Page):
    page.goto("/calculator")
    page.get_by_label("First number").fill("2")
    page.get_by_label("Second number").fill("3")
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_test_id("result")).to_have_text("5")