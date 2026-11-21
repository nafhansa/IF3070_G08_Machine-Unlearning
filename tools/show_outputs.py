"""Cetak output teks setiap sel kode notebook (untuk review cepat). Pakai: python tools/show_outputs.py NB.ipynb"""
import json, sys, re
nb = json.load(open(sys.argv[1]))
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code': continue
    out = []
    for o in c.get('outputs', []):
        if o.get('output_type') == 'stream': out.append(''.join(o['text']))
        elif o.get('output_type') in ('execute_result', 'display_data'):
            d = o.get('data', {})
            if 'text/plain' in d and 'image/png' not in d: out.append(''.join(d['text/plain']))
            elif 'image/png' in d: out.append('[gambar]')
        elif o.get('output_type') == 'error': out.append('ERROR: ' + o['ename'] + ' ' + o['evalue'])
    if out: print(f'--- cell {i}\n' + '\n'.join(out)[:1800])
