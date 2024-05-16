import { Color, COLORS, Image } from "../include/image.js";
import { flipColors, imageMap, mapFlipColors, mapLine, mapToGB, removeRed } from "./imageProcessing.js";

function newWhiteImage(): Image {
  return Image.create(10, 10, COLORS.WHITE);
}

function expectAllPixelsToEqual(image: Image, c: Color): void {
  const pixels = image.pixels();

  pixels.forEach(p => expect(p).toEqual(c));
}

describe("removeRed", () => {
  it("returns a new image and does not modify the original one [PUBLIC]", () => {
    const whiteImage = newWhiteImage();
    const gbImage = removeRed(whiteImage);

    expect(whiteImage).not.toBe(gbImage);
    expectAllPixelsToEqual(whiteImage, COLORS.WHITE);
  });

  it("removes red", () => {
    const whiteImage = newWhiteImage();
    const gbImage = removeRed(whiteImage);

    expectAllPixelsToEqual(gbImage, [0, 255, 255]);
  });

  it("does not change black image", () => {
    const blackImage = Image.create(10, 10, COLORS.BLACK);
    const result = removeRed(blackImage);

    expectAllPixelsToEqual(result, COLORS.BLACK);
  });
});

describe("flipColors", () => {
  it("returns a new image and does not modify the original one [PUBLIC]", () => {
    const whiteImage = newWhiteImage();
    const gbImage = flipColors(whiteImage);

    expect(whiteImage).not.toBe(gbImage);
    expectAllPixelsToEqual(gbImage, COLORS.WHITE);
  });

  it("correctly swap colors", () => {
    const whiteImage = newWhiteImage();
    whiteImage.setPixel(0, 0, [100, 0, 150]);
    const flippedWhiteImage = flipColors(whiteImage);
    const p = flippedWhiteImage.getPixel(0, 0);

    expect(p).toEqual([75, 125, 50]);
  });

  it("does not change black image", () => {
    const blackImage = Image.create(10, 10, COLORS.BLACK);
    const result = flipColors(blackImage);

    expectAllPixelsToEqual(result, COLORS.BLACK);
  });
});

describe("mapLine", () => {
  it("correctly modifies a line [PUBLIC]", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, 5, () => COLORS.BLACK);

    for (let x = 0; x < whiteImage.width; x++) {
      expect(whiteImage.getPixel(x, 5)).toEqual(COLORS.BLACK);
    }
  });

  it("correctly modifies lineNo: 0", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, 0, () => COLORS.BLACK);

    for (let x = 0; x < whiteImage.width; ++x) {
      expect(whiteImage.getPixel(x, 0)).toEqual(COLORS.BLACK);
    }
  });

  it("correctly modifies lineNo: height - 1", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, whiteImage.height - 1, () => COLORS.BLACK);

    for (let x = 0; x < whiteImage.width; ++x) {
      expect(whiteImage.getPixel(x, whiteImage.height - 1)).toEqual(COLORS.BLACK);
    }
  });

  it("does not change anything if lineNo is too high", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, whiteImage.height, () => COLORS.BLACK);

    expectAllPixelsToEqual(whiteImage, COLORS.WHITE);
  });

  it("does not change anything if lineNo is too low", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, -1, () => COLORS.BLACK);

    expectAllPixelsToEqual(whiteImage, COLORS.WHITE);
  });

  it("does not change anything if lineNo is in-bounds but not an integer", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, 5.5, () => COLORS.BLACK);

    expectAllPixelsToEqual(whiteImage, COLORS.WHITE);
  });

  it("does not modify other lines", () => {
    const whiteImage = newWhiteImage();
    mapLine(whiteImage, 5, () => COLORS.BLACK);

    for (let y = 0; y < whiteImage.height; y++) {
      if (y === 5) continue;

      for (let x = 0; x < whiteImage.width; x++) {
        expect(whiteImage.getPixel(x, y)).toEqual(COLORS.WHITE);
      }
    }
  });
});

describe("imageMap", () => {
  it("returns a new image and does not modify the original one [PUBLIC]", () => {
    const whiteImage = newWhiteImage();
    const blackImage = imageMap(whiteImage, () => COLORS.BLACK);

    expect(whiteImage).not.toBe(blackImage);
    expectAllPixelsToEqual(whiteImage, COLORS.WHITE);
  });

  it("returns a similar image", () => {
    const whiteImage = newWhiteImage();
    const blackImage = imageMap(whiteImage, () => COLORS.BLACK);

    expect(blackImage.height).toBe(whiteImage.height);
    expect(blackImage.width).toBe(whiteImage.width);
  });

  it("returns a mapped image", () => {
    const whiteImage = newWhiteImage();
    const blackImage = imageMap(whiteImage, () => COLORS.BLACK);

    expectAllPixelsToEqual(blackImage, COLORS.BLACK);
  });

  it("works on a 10x1 image", () => {
    const whiteImage = Image.create(10, 1, COLORS.WHITE);
    const blackImage = imageMap(whiteImage, () => COLORS.BLACK);
    expectAllPixelsToEqual(blackImage, COLORS.BLACK);
  });

  it("works on a 1x10 image", () => {
    const whiteImage = Image.create(1, 10, COLORS.WHITE);
    const blackImage = imageMap(whiteImage, () => COLORS.BLACK);
    expectAllPixelsToEqual(blackImage, COLORS.BLACK);
  });

  it("works on a 1x1 image", () => {
    const whiteImage = Image.create(1, 1, COLORS.WHITE);
    const blackImage = imageMap(whiteImage, () => COLORS.BLACK);
    expectAllPixelsToEqual(blackImage, COLORS.BLACK);
  });
});

describe("mapToGB", () => {
  it("returns a new image and does not modify the original one [PUBLIC]", () => {
    const whiteImage = newWhiteImage();
    const gbImage = mapToGB(whiteImage);

    expect(whiteImage).not.toBe(gbImage);
    expectAllPixelsToEqual(whiteImage, COLORS.WHITE);
  });

  it("removes red", () => {
    const whiteImage = newWhiteImage();
    const gbImage = mapToGB(whiteImage);

    expectAllPixelsToEqual(gbImage, [0, 255, 255]);
  });

  it("does not change black image", () => {
    const blackImage = Image.create(10, 10, COLORS.BLACK);
    const result = mapToGB(blackImage);

    expectAllPixelsToEqual(result, COLORS.BLACK);
  });
});

describe("mapFlipColors", () => {
  it("returns a new image and does not modify the original one [PUBLIC]", () => {
    const input = Image.create(10, 10, [255, 0, 255]);
    const flippedImage = mapFlipColors(input);

    expect(input).not.toBe(flippedImage);
    expectAllPixelsToEqual(input, [255, 0, 255]);
  });

  it("flip colors", () => {
    const input = Image.create(10, 10, [255, 0, 255]);
    const flippedImage = mapFlipColors(input);

    expectAllPixelsToEqual(flippedImage, [127, 255, 127]);
  });

  it("does not change black image", () => {
    const blackImage = Image.create(10, 10, COLORS.BLACK);
    const result = mapFlipColors(blackImage);

    expectAllPixelsToEqual(result, COLORS.BLACK);
  });
});

test("mapFlipColors and mapToGB do not make needless image copies", () => {
  const spy = jest.spyOn(Image.prototype, "copy");

  const input = Image.create(10, 10, [255, 0, 255]);
  mapFlipColors(input);
  expect(spy).toHaveBeenCalledTimes(1);
  mapToGB(input);
  expect(spy).toHaveBeenCalledTimes(2);
});

afterEach(() => {
  jest.restoreAllMocks();
});
