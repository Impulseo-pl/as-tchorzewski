# Ile da sie oddalic kadr "po": szukamy NAJWIEKSZEGO okna o proporcji pary,
# ktore w calosci lezy na prawdziwych pikselach zdjecia po homografii.
import importlib.util, numpy as np
from PIL import Image, ImageDraw
spec = importlib.util.spec_from_file_location('pm', 'przygotuj-media.py')
pm = importlib.util.module_from_spec(spec); spec.loader.exec_module(pm)
from PIL import ImageOps

N, M = 2500, 1400
po = ImageOps.exif_transpose(Image.open(pm.zrodlo("PO-rozbudowa.jpg"))).convert("RGB").resize((N, N), Image.LANCZOS)
H = pm._homografia(pm.PARY_SUWAKA, pm.WAGI_SUWAKA, N / 1000)
Hm = np.array(list(H) + [1.0]).reshape(3, 3)
przes = np.array([[1, 0, -M], [0, 1, -M], [0, 0, 1]], float)
Hp = (Hm @ przes).ravel(); Hp = (Hp / Hp[8])[:8]
plotno = (N + 2 * M)
poT = po.transform((plotno, plotno), Image.PERSPECTIVE, tuple(Hp), Image.BICUBIC)
maska = Image.new("L", (N, N), 255).transform((plotno, plotno), Image.PERSPECTIVE, tuple(Hp), Image.BICUBIC)
m = np.array(maska) > 200
print("pikseli zdjecia na plotnie:", m.sum())

# sumy prefiksowe -> szybkie sprawdzanie, czy prostokat jest w calosci pokryty
ii = np.cumsum(np.cumsum(m.astype(np.int64), 0), 1)
def pelne(x0, y0, x1, y1):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    if x0 < 0 or y0 < 0 or x1 > plotno or y1 > plotno: return False
    s = ii[y1-1, x1-1] - (ii[y0-1, x1-1] if y0 else 0) - (ii[y1-1, x0-1] if x0 else 0) + (ii[y0-1, x0-1] if x0 and y0 else 0)
    return s == (x1 - x0) * (y1 - y0)

PROP = 1500 / 1239
ys, xs = np.where(m)
print("zakres pikseli: x", xs.min(), xs.max(), " y", ys.min(), ys.max())
skala = N / 1000                      # 1 jednostka skali 0-1000 = tyle pikseli plotna
najlepsze = None
for szer1000 in range(900, 1600, 5):  # szerokosc okna w skali 0-1000
    w = szer1000 * skala; h = w / PROP
    if w > plotno or h > plotno: continue
    for x1000 in range(-300, 400, 5):
        for y1000 in range(-400, 400, 5):
            x = M + x1000 * skala; y = M + y1000 * skala
            if pelne(x, y, x + w, y + h):
                if najlepsze is None or w > najlepsze[0]:
                    najlepsze = (w, h, x1000, y1000, szer1000)
w, h, x1000, y1000, szer1000 = najlepsze
print(f"NAJWIEKSZE OKNO: szerokosc {szer1000} jednostek (OKNO_SUWAKA ma 990), "
      f"lewy gorny rog ({x1000}, {y1000})")
print(f"  -> OKNO_PO = ({x1000}, {y1000}, {x1000+szer1000}, {round(y1000+szer1000/PROP,1)})")
podglad = poT.crop((int(M + x1000*skala), int(M + y1000*skala), int(M + (x1000+szer1000)*skala), int(M + (y1000+szer1000/PROP)*skala)))
podglad.resize((1000, int(1000/PROP))).save("/private/tmp/claude-501/-Users-krzysztof/8b1e1830-cfe4-4395-94c1-880e72ee4e6f/scratchpad/kandydat-po.png")
