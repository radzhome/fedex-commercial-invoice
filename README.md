# Fedex Commercial Invoice #

Fedex Commercial Invoice Generation using Pythong and using reportlab  (Under Development)

### What is this repository for? ###

* A way to generate a commercial fedex invoice without the API
* Version N/A
* https://github.com/radlws/fedex-commercial-invoice

### How do I get set up? ###

* download repo, install requirements.txt using pip

### Usage ###

(TODO, Planning)

* Create an object that gets json params passed to it for creating the invoice. A file can take params and instantiate the object.
* 
<pre><code>
{'company_name': 'TODO', 'company_address': 'TODO', etc...}
</code></pre>

<pre><code>
company_name: 'TODO'
company_address: 'TODO'
waybill_no: 'TODO'
export_date: 'TODO'
export_refs: 'TODO'
shipper: 'TODO'
export_country: 'TODO'
manf_country: 'TODO'
dest_country: 'TODO'

consignee:
  - name
  - address1
  - address2

importer: #(OPTIONAL)
  - name
  - address1
  - address2

fob_caf_cif: 'TODO'

products:
  - { marks_nos: '', no_pkgs: 1, pkg_type: 1, description: 'item described', qty: 1, measure_unit: 'lbs', weight: '25', total_val: '23.24'  }
  - { marks_nos: '', no_pkgs: 1, pkg_type: 1, description: 'item described', qty: 1, measure_unit: 'lbs', weight: '25', total_val: '23.24'  }

signature: 'TODO'
date: 'TODO'
</code></pre>



