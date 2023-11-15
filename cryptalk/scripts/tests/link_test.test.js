/**
 * @jest-environment jsdom
 */

const { getByText } = require('@testing-library/dom');
const buttonClick = require("../tests");

beforeEach(() => {
    document.body.innerHTML = "<p class='m-0 text-center text-white' id='par'></p>";
});

describe("link tests", () => {
    test("Expects content to change", () => {
        buttonClick();
        expect(getByText(document.body, "Follow us").href).toBe("https://www.facebook.com");
    });
});
