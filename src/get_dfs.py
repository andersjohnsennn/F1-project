def get_dfs(dfs):

    circuits = dfs["circuits"]
    constructors = dfs["constructors"]
    constructor_standings = dfs["constructor_standings"]
    drivers = dfs["drivers"]
    driver_standings = dfs["driver_standings"]
    qualifying = dfs["qualifying"]
    races = dfs["races"]
    results = dfs["results"]

    return (
        circuits,
        constructors,
        constructor_standings,
        drivers,
        driver_standings,
        qualifying,
        races,
        results
    )