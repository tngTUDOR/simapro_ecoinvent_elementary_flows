# simapro_ecoinvent_elementary_flows

This repository is a openly-developed and openly-available mapping of the elementary flow lists of ecoinvent 3.8 and SimaPro 9.4.

## Table of Contents

- [Background](#background)
- [Contributing](#contributing)
- [Authors](#authors)
- [Maintainers](#maintainers)
- [License](#license)

## Background

Translating across nomenclature lists is an eternal problem in many problem domains, including life cycle assessment. There have been many ad hoc mapping files and file formats over the years, but recently a large working group produced the [GLAD Elementary Flow Resources](https://github.com/UNEP-Economy-Division/GLAD-ElementaryFlowResources) repository; we will use its data formats for both input files and flow mappings:

* [Input flow lists](https://github.com/UNEP-Economy-Division/GLAD-ElementaryFlowResources/blob/master/Formats/FlowList.md)
* [Output flow mapping](https://github.com/UNEP-Economy-Division/GLAD-ElementaryFlowResources/blob/master/Formats/FlowMapping.md)

Our objective is to improve on the UNEP workflow by making the process of creating the mappings transparent and open to any one who wants to contribute. In addition to other benefits, this should also make future updates easier.

### Simapro `Context` values

To the best of our understanding, the elementary flow list provided by PRé uses a different model for the `Context` value than what is used in ecoinvent. For one thing, they have one UUID for flows, regardless of the subcategory `Context` values. Indeed, the master data list includes only the base `Category` values, namely:

* 'Airborne emissions'
* 'Economic issues'
* 'Emissions to soil'
* 'Final waste flows'
* 'Non material emissions'
* 'Raw materials'
* 'Social issues'
* 'Waterborne emissions'

They also use slightly different names for these base `Context` values, e.g. for `Airborne emissions`:

* In the master flow list: Airborne emissions
* In an LCI file: Emissions to air
* In an LCIA file: Air

We use the LCI file version, as this is the most common use case for data conversion. These are (again, to the best of our knowledge):

* Emissions to air
* Economic issues
* Emissions to soil
* Final waste flows
* Non material emissions
* Resources
* Social issues
* Emissions to water

### `Context` mapping

Here is our current mapping for different base `Context` values

#### Water

| ecoinvent context | Simapro context | Match condition (Simapro to ecoinvent) |
| ----------------- | --------------- | -------------------------------------- |
| water/fossil well | Emissions to water/groundwater, long-term | ~ |
| water/ground- | Emissions to water/groundwater | = |
| water/ground-, long-term | Emissions to water/groundwater, long-term | = |
| water/ocean | Emissions to water/ocean | = |
| water/surface water | Emissions to water/lake | < |
| water/surface water | Emissions to water/river | < |
| water/surface water | Emissions to water/river, long-term | < |
| water/unspecified | Emissions to water/(unspecified) | = |

## Contributing

We follow the [Github Flow, a workflow based around pull requests](https://docs.github.com/en/get-started/quickstart/github-flow), and use Github actions to do quality assurance. The Github flow documentation covers the basics; to make a contribution here you will need to:
So, if you want to contribute you need to:

* Write some code to create CSVs following the [Output flow mapping](https://github.com/UNEP-Economy-Division/GLAD-ElementaryFlowResources/blob/master/Formats/FlowMapping.md) format. You can also do mappings manually, though we would prefer you to automate this as much as possible, so that we can easily change or regenerate the mappings if needed. The repo includes a [template for doing matching](https://github.com/brightway-lca/simapro_ecoinvent_elementary_flows/blob/main/Notebooks/Template%20matching%20notebook.ipynb), and the folder `Notebooks` includes matching notebooks that have been incorporated into the current data.
* However you generate it, you must create a CSV with new mappings **in the `Contribute` directory**.
* Create a pull request, using the `new_mapping` template. Make sure you have done the tasks given in the template; you can always update your pull request with new commits!
A contributor forks this repository and adds their mapping contribution as a new CSV file in the `Contribute` directory. Ideally these contributions will be generated programmatically, either via a Jupyter Notebook (added to `Notebooks`) or a script (added to `Scripts`).
* They create a pull request, which triggers Github Actions which check the validity of their mapping file, and checks whether the new mappings contradict existing mappings. If there are errors, an error log is created and attached to the pull request.
* If the pull request is accepted, a separate set of Github Actions are run which merge the new mappings into `Mapping/Output/Mapped_files`, and updates the `README.md` file and status reports.

## Status

Current status is reported in the file: [status.md](status.md)

## Contributing

Your contributions are welcome! This effort, and indeed consistent, high-quality LCA results, are only possible when we work together.

You will need a Github account.

Additions to the existing mapping are done using Github Actions, and can be done manually or programmatically. If you are interested in contributing, please first check the `Status` directory, whose readme file describes the number and types of flows already mapped.

Contributions should come as pull requests from named branches. So, you should:

* Fork this repo
* Create a new branch with a descriptive name
* Work work work, and then commit
* Create a Pull Request, and put `@cmutel` in the Pull Request description

## Authors

{{ authors }}

## Maintainers

* [Chris Mutel](https://github.com/cmutel/)
* [Tomás Navarrete](https://github.com/tngtudor)

## License

* Code: [BSD-3-Clause](https://github.com/brightway-lca/bw_processing/blob/master/LICENSE)
* Data: [Open Data Commons Public Domain Dedication and License v1.0](http://opendatacommons.org/licenses/pddl/)
