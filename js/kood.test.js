const matemaatilisedArvutused = require('./kood');

it("should multiply correctly", () => {
    const result = matemaatilisedArvutused(10, 5);
    expect(result.korrutis).toBe(50);
});