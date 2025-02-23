# Test Plan

### 1. File Loading
   - Load **`planets_data.json`** and ensure it exists and contains valid JSON.
   - Test behavior when **`planets_data.json`** is missing or corrupted.

### 2. Basic Functional Tests
   - Query: "Tell me everything about Saturn?"
     - Expected: Complete information about Saturn.
   - Query: "How massive is Neptune?"
     - Expected: "Neptune has a mass of X kg."
   - Query: "Is Pluto in the list of planets?"
     - Expected: "Pluto is not a planet."
   - Query: "How many moons does Earth have?"
     - Expected: "Earth has X moons."

### 3. Error Handling
   - Query: "Tell me everything about **XYZ?**"
     - Expected: "Planet not found."
   - Query: "How massive is ?"
     - Expected: "Sorry, I didn't understand your query."

### 4. Case Insensitivity Test
   - Query: "tell me everything about jupiter?"
     - Expected: Should return the correct Jupiter data.

### 5. Exit Condition
   - Enter "exit"
     - Expected: Program should terminate gracefully.

### 6. Edge Cases
   - Empty input: `""`
   - Whitespace input: `"   "`
   - Misspelled planet names: `"Neptun"` instead of `"Neptune"`
   - Extra spaces in queries: `"  how massive is   Mars   "`
