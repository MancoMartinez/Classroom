# Appriss — Ingeniería (docs fuente)

Carpeta 14 de la base de Moscú. 244 fragmentos.

## PlatformUI — Claude Instructions · What is PlatformUI?
_chunk 375 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

**PlatformUI** is the main ASP.NET Core MVC application that hosts all Secure platform UI functionality. It serves:
- Razor views that bootstrap React micro-apps
- REST APIs consumed by those React apps
- Legacy AngularJS and jQuery pages (being phased out)

---

## PlatformUI — Claude Instructions · Architecture Overview
_chunk 376 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

PlatformUI follows the **Areas pattern** for modular organization:

```
PlatformUI/
├── Areas/                  # Feature modules (50+ areas)
│   ├── <FeatureName>/
│   │   ├── Controllers/    # API + View controllers
│   │   ├── Views/          # Razor views (.cshtml)
│   │   ├── Models/         # Request/response DTOs
│   │   ├── Services/       # Business logic (optional)
│   │   └── Filters/        # Action filters (optional)
│   └── ...
├── Views/
│   └── Shared/             # Shared layouts (_ThinLayout, _Layout, etc.)
├── Common/                 # Shared utilities
└── Program.cs              # App startup
```

---

## PlatformUI — Claude Instructions · Controller Patterns
_chunk 377 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

### Two Controller Types

Every Area typically has two controllers:

| Type | Base Class | Purpose | Example Route |
|---|---|---|---|
| **ViewController** | `CpfControllerCore` | Returns Razor views | `GET /incident` |
| **ApiController** | `ApiControllerCore` | REST API endpoints | `POST /incident/api/v1/incidents` |

### ApiControllerCore (API Controllers)

Base class for all API endpoints. Located at `Sources/UI/Components/Contract/ApiControllerCore.cs`.

```csharp
[Area("incident")]
[Route("incident/api")]
[ApiController]
public class IncidentController(IDirector director) : ApiControllerCore(director)
{
    [HttpGet("v1/incidents")]
    public ActionResult GetIncidents(CancellationToken cancellationToken)
    {
        try
        {
            // Business logic
            ResultBag resultBag = new ResultBag(true, data);
            return new JsonActionResult(resultBag);
        }
        catch (Exception ex)
        {
            return this.Error(ex);  // Standardized error handling
        }
    }
}
```

Key features:
- **`IDirector` injection** — Access to configuration, user context, resources
- **`this.Error(ex)`** — Standardized exception handling → `ResultBag` response
- **`JsonActionResult`** — Wraps data in `ResultBag` format
- **`this.NoPermissionResult()`** — Returns 200 with `NoPermission: true` flag
- **`CancellationToken`** — Always pass through for async operations

### CpfControllerCore (View Controllers)

Base class for Razor view controllers. Located at `Sources/UI/Components/Contract/CpfControllerCore.cs`.

```csharp
[Route("incident")]
[IncidentEnabled]  // Custom filter
public class ViewController : CpfControllerCore
{
    public ActionResult Index()
    {
        return this.View("~/areas/Incident/views/index.cshtml");
    }
}
```

Key features:
- Inherits from `Controller` (not `ControllerBase`)
- Returns `this.View()` pointing to Razor templates
- Often uses custom filters like `[IncidentEnabled]` for feature gating

---

## PlatformUI — Claude Instructions · Response Format
_chunk 378 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

All API responses use the standardized `ResultBag` wrapper:

```json
{
    "Success": true,
    "Data": { ... },
    "Message": null,
    "Token": null
}
```

On error:
```json
{
    "Success": false,
    "Data": null,
    "Message": "Error message",
    "Token": "correlation-guid"
}
```

React apps check `response.Success` before processing `response.Data`.

---

## PlatformUI — Claude Instructions · Razor Views
_chunk 379 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

### Layout Structure

All views use shared layouts in `/Views/Shared/`:

| Layout | Use Case |
|---|---|
| `_ThinLayout.cshtml` | React app host (minimal chrome) |
| `_Layout.cshtml` | Full page layout |
| `_DynoLayout.cshtml` | DynoView pages |

### React App Host Pattern

Most modern views are thin Razor shells that bootstrap React:

```cshtml
@using ApprissRetail.Components.Contract
@inherits CpfWebViewPage

@{
    this.Layout = "/Views/Shared/_ThinLayout.cshtml";
}

@section scripts
{
    <script src="@this.Url.CpfContent("~/_react/dist/incident.js", this.Director)"></script>
}

@section ribbon
{
    <div id="react-toolbar-root"></div>
}

@section subnav
{
    <div id="react-sidebar-root"></div>
}

<div id="react-app-root"></div>
```

Key conventions:
- **`@inherits CpfWebViewPage`** — Required for platform helpers
- **`@this.Url.CpfContent()`** — Cache-busted asset URLs
- **`this.Director`** — Access to user/config context in views
- **Sections** — `scripts`, `ribbon`, `ribbonright`, `subnav` slots

### Passing Data to React

Server data is passed via `window` globals set in the Razor view:

```cshtml
<script>
    window.INCIDENT_CONFIG = @Html.Raw(Json.Serialize(Model.Config));
</script>
```

Or via hidden inputs that React reads on mount:

```cshtml
<input type="hidden" id="currency-symbol" value="@Model.Currency.Symbol" />
```

---

## PlatformUI — Claude Instructions · Key Areas
_chunk 380 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

| Area | Purpose | Has API | Has Views |
|---|---|---|---|
| `Incident` | Case management | Yes | Yes |
| `EngageMetrics` | Engage Insights dashboard | Yes | Yes |
| `EngageInsights` | Consumer profile | Yes | Yes |
| `Workview` | Investigation workbench | Yes | Yes |
| `Dashboards` | Dashboard viewer | Yes | Yes |
| `Designer` | UI designer tools | Yes | Yes |
| `Cpf` | Core platform (auth, search) | Yes | Yes |
| `QuickEntry` | Quick incident entry | Yes | Yes |
| `Sidekick` | AI assistant (chat, analysis, OOTB tiles) | Yes | Yes |

---

## PlatformUI — Claude Instructions · IDirector Interface
_chunk 381 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

The `IDirector` is the central dependency for all platform operations:

```csharp
public interface IDirector
{
    IConfiguration Configuration { get; }      // App config
    IGlobalConfiguration GlobalConfiguration { get; }  // Global config
    IUser User { get; }                        // Current user context
    IResources Resources { get; }              // i18n resources
    IRepo Repo { get; }                        // File/repo operations
    int UserID { get; }                        // Current user ID
    // ... and more
}
```

Usage patterns:
```csharp
// Check feature flag
bool enabled = this.Director.Configuration.GetConfigItem("Feature.Incident", true);

// Get localized string
string label = this.Director.Resources.Get(ResourceKey.SaveButton);

// Check permission
bool canView = this.Director.User.UserHasPermission(userId, permissionPath, "CanView");
```

---

## PlatformUI — Claude Instructions · Custom Filters
_chunk 382 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

Areas often define custom action filters:

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method)]
public class IncidentEnabled : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        // Check if Incident module is enabled for this client
        // Redirect or return 404 if not
    }
}
```

Common filters:
- `[IncidentEnabled]` — Check Incident module is active
- `[ClaimsAuthEnabled]` — Check Claims module is active
- Custom permission checks

---

## PlatformUI — Claude Instructions · Naming Conventions
_chunk 383 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

| File | Pattern |
|---|---|
| API controller | `*ApiController.cs` or `ApiController.cs` |
| View controller | `ViewController.cs` or `*Controller.cs` |
| Index view | `Index.cshtml` |
| Partial view | `_PartialName.cshtml` |
| Model | `*Request.cs`, `*Response.cs`, `*ViewModel.cs` |
| Service | `*Service.cs`, `I*Service.cs` |

---

## PlatformUI — Claude Instructions · Route Patterns
_chunk 384 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

### API Routes

```
/{area}/api/v{version}/{resource}
/{area}/api/v{version}/{resource}/{id}
/{area}/api/v{version}/{resource}/{id}/{action}
```

Examples:
- `GET /incident/api/v1/incidents`
- `GET /incident/api/v1/incidents/123`
- `POST /incident/api/v1/incidents/123/close`

### View Routes

```
/{area}                    → Index action
/{area}/{action}           → Named action
/{area}/{controller}/{action}  → Explicit controller
```

Examples:
- `GET /incident` → `ViewController.Index()`
- `GET /engagemetrics` → `ViewController.Index()`

---

## PlatformUI — Claude Instructions · Creating a New Area
_chunk 385 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

1. Create folder: `Areas/<FeatureName>/`
2. Add controllers:
   - `Controllers/ViewController.cs` (extends `CpfControllerCore`)
   - `Controllers/ApiController.cs` (extends `ApiControllerCore`)
3. Add views:
   - `Views/Index.cshtml` (with `_ThinLayout` for React)
4. Add models:
   - `Models/<Request/Response>.cs`
5. Register in webpack if React app:
   - Add entry in `webpack.config.js`
6. Add route/menu link in platform navigation

---

## PlatformUI — Claude Instructions · Common Tasks
_chunk 386 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

### Add a new API endpoint

1. Add method to existing `*ApiController.cs` or create new controller
2. Use `[HttpGet]`, `[HttpPost]`, etc. with route template
3. Accept `CancellationToken` for async work
4. Return `JsonActionResult(new ResultBag(true, data))`
5. Wrap in try/catch, use `this.Error(ex)` for errors

### Add a new Razor view for React

1. Create `Views/Index.cshtml` in the Area
2. Set layout to `_ThinLayout.cshtml`
3. Add `@section scripts` with React bundle
4. Add root `<div id="react-app-root"></div>`
5. Pass server data via `window` globals or hidden inputs

### Check user permissions

```csharp
if (!this.Director.User.UserHasPermission(this.Director.UserID, permissionPath, "CanView"))
{
    return this.NoPermissionResult();  // For API
    // OR
    return this.NoPermission();  // For views (redirect)
}
```

---

## PlatformUI — Claude Instructions · Testing
_chunk 387 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

Controller tests should mock `IDirector` and its sub-interfaces:

```csharp
[TestMethod]
public void GetIncidents_ReturnsSuccessResult()
{
    // Arrange
    var mockDirector = new Mock<IDirector>();
    var controller = new IncidentController(mockDirector.Object);

    // Act
    var result = controller.GetIncidents(CancellationToken.None);

    // Assert
    var jsonResult = Assert.IsType<JsonActionResult>(result);
    Assert.True(((ResultBag)jsonResult.Value).Success);
}
```

---

## PlatformUI — Claude Instructions · Related Documentation
_chunk 388 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE (1).md_

- React micro-apps: `Sources/UI/Components/src/_react/CLAUDE.md`
- Engage Insights: `Sources/UI/Components/src/_react/src/apps/engage-metrics/CLAUDE.md`
- Main platform guide: `/CLAUDE.md`

## React Codebase — Claude Instructions · Project Overview
_chunk 389 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

This is a large-scale React application composed of **66 independent micro-app bundles**, all compiled from a single codebase via Webpack. Apps live in `src/apps/`, shared utilities in `src/shared/`.

## React Codebase — Claude Instructions · Commands
_chunk 390 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

```bash
npm run dev          # Development build with watch mode
npm run build        # Production build
npm run test         # Run tests with coverage
npm run test-update  # Update snapshots
npm run lint         # Check linting
npm run lint-fix     # Auto-fix linting issues
```

Coverage threshold is 53% (branches, functions, lines, statements). Tests must pass this threshold.

### Always run `npm run lint-fix` after touching React code

Whenever you finish editing files under `src/` (components, services, tests, constants — anything in this React tree), run `npm run lint-fix` from `Sources/UI/Components/src/_react` before reporting the work as done. The auto-fixer reformats long JSX, collapses multi-line ternaries, sorts imports, and applies the project's Prettier rules; skipping it leaves diffs that the linter will rewrite on the next CI build or developer commit.

This is a default, not a suggestion — run it even if the changes look small.

## React Codebase — Claude Instructions · Project Structure
_chunk 391 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

```
src/
├── apps/           # 50+ feature micro-apps, each with its own webpack entry point
├── shared/
│   ├── components/ # Reusable UI components
│   ├── hooks/      # Custom React hooks
│   ├── services/   # Business logic and HTTP utilities
│   ├── models/     # Data structures
│   └── styles/     # Global styles and theme
└── constants.js    # Global RESX resource strings (i18n)
```

Each app in `src/apps/` is self-contained:
```
src/apps/<feature>/
├── index.js          # App entry point and router
├── constants.js      # App-specific constants
├── context.js        # React Context (if needed)
├── components/       # Feature components
└── services/         # Feature business logic
```

## React Codebase — Claude Instructions · Tech Stack
_chunk 392 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

- **React 18** with React Router 6 (hash-based routing)
- **Webpack 5** — one bundle per app, output to `../../wwwroot/_react/dist/`
- **Jest 29** + Testing Library for tests
- **Bootstrap 5** + **React Bootstrap** + **Tailwind CSS 4** for styling
- **CSS Modules** for component-scoped styles
- **PropTypes** for runtime type checking (no TypeScript)
- **ESLint + Prettier** for linting and formatting

## React Codebase — Claude Instructions · Code Conventions
_chunk 393 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

### File Naming

| Type | Pattern |
|---|---|
| Components | `component-name.js` or `component-name.component.js` |
| Services | `service-name.service.js` |
| CSS Modules | `component-name.module.css` |
| Tests | `*.test.js` |
| App entry | `index.js` |
| Context | `context.js` |
| Constants | `constants.js` |

All filenames use **kebab-case**.

### Components

All new components must be **functional components**. Class components exist in legacy shared components — do not add new ones.

```javascript
export function MyComponent({ label, onClick }) {
    return <div onClick={onClick}>{label}</div>;
}

MyComponent.propTypes = {
    label: PropTypes.string.isRequired,
    onClick: PropTypes.func
};
```

Always add **PropTypes** to every component. Use named exports for components, default exports for services.

### Styling

Use **CSS Modules** for component styles:
```javascript
import styles from './my-component.module.css';

<div className={styles.container}>
```

- Files ending in `.module.css` are automatically scoped
- `src/shared/styles/theme.css` is a global stylesheet — do NOT use CSS Modules syntax there
- Bootstrap and Tailwind utility classes are fine to use alongside CSS Modules

### Path Aliases

```javascript
import Foo from '@shared/services/foo/foo.service';
import Bar from '@engage-shared/...';
import Baz from '@claims-auth/...';
```

Prefer aliases over long relative paths when importing from `src/shared/`.

### State Management

No Redux or Zustand. State is managed via:
1. **React Context** — for app-level shared state (see existing `context.js` files)
2. **Local component state** — `this.state`/`useState` for UI state
3. **Service classes** — stateful services instantiated in context or at module level
4. **`window` globals** — read-only environment config: `HTTP`, `APPLICATIONPATH`, `USERID`, `CULTURE`, `STYLEOPTION`, `THEME_COOKIE_VALUE`, `moment`

### Routing

Apps use hash-based routing:
```javascript
import { createHashRouter } from 'react-router-dom';
const router = createHashRouter([{ path: '/edit', element: <EditView /> }]);
```

## React Codebase — Claude Instructions · Testing
_chunk 394 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

- Use `@testing-library/react` for component tests
- Use snapshot tests for rendering assertions
- Follow the AAA pattern (Arrange, Act, Assert)
- Wrap state-changing interactions in `act()`
- Use `data-testid` attributes for element selection in tests
- CSS imports are stubbed automatically — no need to mock them

## React Codebase — Claude Instructions · Server-Replaced Tokens (i18n, Config)
_chunk 395 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

String constants in JS files use special tokens that a server-side handler replaces when the compiled bundle is requested in the browser. There are three formats:

### $RESX strings — `$RESX('area', 'key', 'default')`

**Use `$RESX` by default for all new localised labels.** Each app and the global `src/constants.js` define these.

```javascript
$RESX('Sysrepublic.Foundation.CPF.CpfResources', 'DataError', 'Something went wrong while trying to load the data')
```

- **area** — the .NET resource class (first argument)
- **key** — the resource key (second argument)
- **default** — fallback text (third argument)

Replaced at serve-time with the translated value for the user's culture. The **unique identifier** is `area + key` — the default is only a fallback.

### RESOURCE strings — `RESOURCE{{area}:{key}:{default}}`

Alternative syntax for localised labels, same behaviour as `$RESX(...)`. Existing code may use this format; do not rewrite it just for the sake of consistency, but prefer `$RESX` for any new entries.

```
RESOURCE{{Sysrepublic.Secure.UI.Areas.Incident.IncidentResources}:{Address}:{Address}}
```

- **area** — the .NET resource class (e.g. `Sysrepublic.Secure.UI.Areas.Incident.IncidentResources`)
- **key** — the resource key within that class
- **default** — fallback text shown if no translation exists

The same duplicate rules apply — `area + key` is the unique identifier.

### $CONFIG strings — `$CONFIG('key', 'default')`

Used for configuration values (not labels). Replaced at serve-time with the config value for the current tenant.

```javascript
$CONFIG('Explorer.Export.MaxNumbRecipientsForEmail', '20')
```

- **key** — the configuration key (first argument)
- **default** — fallback value if the config key is not set (second argument)

### Where to define $RESX / RESOURCE strings

- **`src/constants.js`** (root) — shared/common resources used across multiple apps. Labels like "OK", "Yes", "No", "Cancel", "Dismiss", "Save", "New", "Add to Investigation", etc. belong here. These take priority and should be imported by any app that needs them.
- **`src/apps/<feature>/constants.js`** — app-specific resources that are only used within that app. A resource should only live here if it is genuinely specific to the feature and not used elsewhere.

### Rules for $RESX / RESOURCE strings

1. **No duplicate area:key pairs across the entire app.** Not just within a single file — across all constants files. If two entries share the same area and key but have different defaults, the parser takes the **last** defined value and applies it everywhere that area:key appears. This means:
   - The Delivery team may update the wrong entry when customising a label for a client, causing it to change in the wrong place.
   - A default mismatch silently overrides the earlier definition.
2. **Check root `src/constants.js` first.** Before adding a new entry, check whether a shared constant already exists. Import from there rather than re-declaring.
3. **Check other app constants files too.** If the resource you need already exists in another app's constants file, consolidate it — move it to `src/constants.js` so both apps can share it.
4. **Minimise entries with the same default value.** If an existing resource anywhere in the app already resolves to the same text, re-use it rather than adding a new one.
5. **Consolidate when duplication appears.** If an app-specific resource starts being used by a second app, move it to `src/constants.js`.
6. **If you cannot re-use, make the key unique.** Prefix or suffix the key to distinguish it (e.g. `AddressLine1` vs `AddressSearch`).
7. **Keep constants files tidy.** When adding entries, check for and remove any duplicates you find.

## React Codebase — Claude Instructions · Angular Integration
_chunk 396 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

This codebase runs alongside a legacy Angular app. Be careful when:
- Accessing `window.angular` or the Angular injector
- Dispatching/listening to custom DOM events used by Angular
- Modifying global `window.*` properties used by both layers

## React Codebase — Claude Instructions · Key Shared Services
_chunk 397 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

| Service | Purpose |
|---|---|
| `CommonService` | Dates, colors, downloads, localStorage utilities |
| `HTTPService` | All API calls |
| `DependenciesService` | Dependency tracking |
| `ValidationService` | Form validation |
| `PendoService` | Analytics/telemetry |

## React Codebase — Claude Instructions · Shared Component Usage Notes
_chunk 398 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/CLAUDE.md_

### `LocalDataFilteredSelect`

**`value` is always an array.** The component's PropTypes declare `value: PropTypes.array` and the internal render iterates over it directly. Passing a single object or `null` will throw a PropTypes warning and break display.

**`onChange` always receives an array.** For single-select, it will be `[]` (cleared) or `[selectedOption]`.

Use these helpers — copy them into any component that uses `LocalDataFilteredSelect`:

```javascript
// Convert stored scalar value → array for the value prop
function toSelectValue(options, value) {
    const match = options.find((opt) => opt.value === String(value));
    return match ? [match] : [];
}

// Convert array from onChange → scalar for state
function fromSelectValue(selected) {
    return selected[0]?.value ?? '';
}
```

Usage in JSX:

```jsx
<LocalDataFilteredSelect
    id='my-field'
    label='My Field'
    value={toSelectValue(MyOptions, form.myField)}
    options={MyOptions}
    onChange={(selected) => setField('myField', fromSelectValue(selected))}
/>
```

For **multi-select** (`multiple={true}`), `value` and `onChange` payloads are already arrays of option objects — no conversion helpers needed.

## Verify Database · Overview
_chunk 399 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/README.md_

Verify Database is the main repository for the TRE_RETURN_XX applications. It contains all the core data structures,
including tables, views, stored procedures, functions, and security objects. The database is responsible for storing and
managing data related to all Engage modules.

## Verify Database · Project Structure
_chunk 400 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/README.md_

This project contains all the SQL scripts for all objects in the TRE_RETURN_XX databases.

- assemblies - Contains the .NET CLR assembly that has the hashing functionality used through the Engage database.
- security - Contains all the security-related scripts, including users, roles, and permissions.
- functions - Contains all the user-defined functions.
- sp - Contains all the stored procedures.
- views - Contains all the views.
- tables - Contains all the table definitions.
- types - Contains all the user-defined table types.
- triggers - Contains all the triggers.
- releases - Contains subfolders for each production release, where each subfolder contains a list of objects to deploy
in a release, including release specific scripts.
- Verify1DatabaseCLR - Contains the SQL project for the CLR assembly.

## Verify Database · Local Development
_chunk 401 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/README.md_

All development should be done in a local or shared development database. Changes should be tested locally before being 
committed to source control. Engineers will be assigned a dedicated or shared DB server. Work with the DBA team for a server assignment.

Databases on the dev servers are a snapshot of production. Snapshots can be refreshed on demand by running the PureArary
command line tool on the dev server. Running the tool should be self-explanatory, but reach out to the DBA team for help
if needed.

### Idempotent Scripts
All scripts should be idempotent, meaning that they can be run multiple times without causing errors or changing the
result beyond the initial application. This is typically achieved by checking for the existence of an object before
creating or altering it. View the tables scripts for examples of idempotent script patterns.

## Verify Database · Branching Strategy
_chunk 402 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/README.md_

Feature branches should be named using format user/work-item/short-description. For example, kvu/TREVERI-1234/add-new-monitor.
Feature branches should branch off the current sprint branch and PR back into the current sprint branch.
As the release nears, the sprint branch will be merged into the release branch.

Sprint branches should be named sprint_[year].[month].[day] where the year, month, and date correspond to the deploy date of the sprint.
Sprint branches can be created by anyone on the team, branching off of release.

## Verify Database · Build and Release
_chunk 403 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/README.md_

Release artifacts are defined by creating subfolders under the releases folder. Each release subfolder contains a list of
objects to deploy in a release, including release specific scripts. Release folders should be named using the format
verify_[year].[month].[day] where the year, month, and date correspond to the planned release date.

Within the release specific folder, you may have a scripts folder that contains any scripts that are specific to that release.
The release folder should also contain a deploy_files.txt file that lists all the objects to be deployed in the release in the
order they should be deployed. View previous releases for examples. If the release contains new objects, the release folder
should also contain a replication_files.txt file that lists all the new objects to be replicated to replicated DB copies.

### Build and Release Pipelines
Use build pipeline build-engagedatabase-production (https://apprissretail.visualstudio.com/VerifyDatabase/_build?definitionId=209).
The pipeline must be run manually. During the sprint, build the sprint branch. The build pipeline has a parameter named 
"Verify Build Number" - specify the [year].[month].[day] of the sprint branch you are building; this is used to grab the correct
release artifacts. Near the end of the sprint, build the release branch.

The build automatically triggers the release pipeline deploy-engagedatabase-production.

### Handoff to QA
Once the build succeeds, notify the QA team to begin testing. Provide the work item(s) and link to the release pipeline.

## Verify Database · Adding Monitors
_chunk 404 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/README.md_

### Adding a RobustDriftMonitor

Many of the Engage metric monitors set up in this repo are of the RobustDriftMonitor type, which
monitors if a metric of interest is outside of the IQR (Interquartile Range) of the metric's historical values for some
number of days. This is simply the boxplot definition of an outlier and is a robust way to detect drift in a metric.

To add a new metric monitor of this type, you need to do two things:

1. Add a new file in `src/functions` named `Monitoring.Daily<MetricName>.sql` containing a function that calculates the
   metric
   of interest for a given retailer for each day between some start and end date and returns two columns, containing the
   date and metric for a given day. The procedure should have the following signature:
   ```sql
    ALTER FUNCTION Monitoring.Daily<MetricName>(retailer_id INT, start_date DATE, end_date DATE)
    ```
   See `src/function/Monitoring.DailyActionRate.sql` for an example.
2. In `src/sp/Monitoring_RobustDriftMonitor.sql`, add a new case metric switch statement starting at line 61 that calls
   the function you just created. The case should look like this:
   ```sql
    ELSE IF @metric = '<MetricName>'
        BEGIN
            INSERT INTO #DailyStatistic
            SELECT date, statistic
            FROM Monitoring.Daily<MetricName>(@retailer_id, @start_date, @current_date);
        END;
   ```

## AI Outliers · Overview
_chunk 405 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

AI Outliers uses unsupervised machine learning to detect unusual patterns in store and cashier transaction data. It identifies entities whose behaviour differs significantly from peers, then surfaces results on profile pages and as work items.

This document covers the technical architecture. For operational guides, see Confluence:
- [AI Outliers - Cashier and Store](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474832896009) — feature overview
- [AI Outliers - Configuration](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474741833731) — all feature flags and config items
- [AI Outliers - Monitoring & Analysis](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/477467017226) — monitoring run health
- [AI Outliers - Failure Runbook](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475383758857) — triage and resolution
- [AI Outliers - Design](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474609614859) — original design document

---

## AI Outliers · Architecture
_chunk 406 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

```
Metric Database (Snowflake / Greenplum)
    ↓
Python FastAPI (Azure Functions) — IsolationForest + SHAP
    ↓
Azure Table Storage (results storage)
    ↓
SecureAI Work Item Generator (.NET, HATR) — reads results, creates work items
    ↓
workview.Workview (Platform DB) + workview.WorkItemPopulationOutlierResults/Reasons
    ↓
UI — Store/Cashier profile pages, Top Outliers dashboard, Work Item queue
```

---

## AI Outliers · Choosing Metrics for AI Outliers
_chunk 407 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

AI Outliers runs on **metrics** — period-aggregated KPIs grouped by store or cashier. See `metric-generation.md` for how metrics are calculated and stored. Admins control which metrics are included in the IsolationForest model via tags in the Metric Manager UI.

### Tags

Two tags control inclusion:

| Tag | Key requirement | Purpose |
|---|---|---|
| `secureai-store` | Key1 = store only | Include in store outlier analysis |
| `secureai-cashier` | Key1 = store AND Key2 = cashier | Include in cashier outlier analysis |

Constants: `Sources/Core/Core/SecureAI/Outliers/Models/SecureAiMetricTags.cs`

### How Metrics Are Enabled

1. **Admin toggles in Metric Manager UI** — each metric definition has `StoreProfileSecureAiEnabled` and `CashierProfileSecureAiEnabled` checkboxes
2. **MetricManagerService** updates the `Tags` field — `SetStoreProfileTags()` / `SetCashierProfileTags()` adds or removes the tag from a space-separated string
3. **Persisted to database** — `METRIC_METRICDEFINITIONUPDATE` writes the updated Tags to `METRIC_METRICDEFINITION.TAGS`

Key validation during save:
- Store outliers require the metric to have `Key1KeysetID = 1` (store key)
- Cashier outliers require `Key1KeysetID = 1` AND `Key2KeysetID = 2` (store + cashier keys)

Service: `Sources/UI/UI/Areas/MetricManager/Core/MetricManagerService.cs` (lines 658–746)

### How Tagged Metrics Are Discovered at Runtime

`SecureAiMetricService` (`Sources/Core/Core/SecureAI/Outliers/Services/SecureAiMetricService.cs`) provides:

1. **`GetSecureAiTaggedMetricDefinitions(calendarVfp, periodType, tag)`** — queries all metric definitions for the calendar/period, filters by `Tags.Contains(tag)`, caches the result
2. **`ValidateTaggedMetricDefinitionsAndGetKeySetId(metrics, tag)`** — validates:
   - Minimum 2 metrics tagged (IsolationForest needs multiple features)
   - All tagged metrics have matching key structure (same KeysetIDs)
   - Returns the most specific KeySetId (store or cashier grain)

The `SecureAiDefinitionRequestProcessor` then extracts the metric IDs from the tagged definitions and passes them to the Python API:

```
metricIds = taggedMetrics.Select(m => m.ID).ToArray()
→ sent to Python API as comma-separated parameter
→ Python queries metric values for these IDs from the database
→ IsolationForest trains on the resulting feature matrix
```

### Metric Definition Storage

Metric definitions and their schema are documented in `metric-generation.md`. The fields most relevant to AI Outliers are `Tags` (controls inclusion via `secureai-store`/`secureai-cashier`), `Key1KeysetID`–`Key4KeysetID` (must match across all tagged metrics), and `PeriodType` (determines which periods are analysed).

---

## AI Outliers · Python API
_chunk 408 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

**Location:** `Sources/PythonApi/ai_outliers/`

The API runs as an Azure Functions app with four HTTP endpoints and a queue trigger.

### Endpoints

| Method | Route | Purpose |
|---|---|---|
| GET | `/ai_outliers/view/{env}/{client}/{key_type}/{period_type}` | Available periods for analysis |
| GET | `/ai_outliers/api/{env}/{client}/{key_type}/{period_type}/{year}/{period}/{key?}` | Retrieve outlier results |
| POST | `/ai_outliers/api/outlier_analysis` | Direct analysis on provided data |
| DELETE | `/ai_outliers/api/{env}/{client}/{key_type}/{period_type}/{year}/{period}/{key?}` | Invalidate cached results |

### Queue Trigger

- **Queue name:** `{deploymentSlot}-ai-outlier-queue`
- **Trigger:** Queue message with row key identifying the analysis request
- **Timeout:** 2.5 hours (host.json)
- **Batch size:** 2 messages, max 5 retries

### Key Files

| File | Purpose |
|---|---|
| `ai_outliers_blueprint.py` | HTTP endpoints and queue trigger |
| `outlier_ai.py` | ML model core — IsolationForest fitting, SHAP computation |
| `azure_table_utils.py` | Table Storage I/O, boundary calculations, job orchestration |
| `custom_types.py` | Request/response dataclasses (SecureAIRequest, KeyType, PeriodType) |
| `function_app.py` | Azure Functions host with New Relic integration |

### Key Types

```python
class KeyType(Enum):
    storeno = 1
    cashierno = 2

class PeriodType(Enum):
    week = 64
    month = 128
    quarter = 256
    year = 512
```

---

## AI Outliers · ML Model
_chunk 409 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

**Algorithm:** Isolation Forest (scikit-learn) — unsupervised anomaly detection.

**Feature importance:** SHAP (TreeExplainer) — computes per-metric contribution to each entity's outlier score.

### Training Flow

1. Load metric data from database, filtered by tags (`secureai-store` or `secureai-cashier`)
2. Remove constant-value columns (no variance)
3. Normalise metrics using "BASE COUNT" metric if available
4. Fit IsolationForest (`random_state=0`)
5. Compute anomaly scores and predictions
6. Calculate SHAP values for explanation
7. Generate percentile-based boundaries (amber = top X%, red = top X/10%)

### Result Storage

Results are cached in **Azure Table Storage** with table names derived from request parameters:

```
{environment}c{client_id}kt{key_type}pt{period_type}{year}{period}md5{hash}
```

Each table contains:
- `__response` row — overall analysis metadata
- Per-entity rows — SHAP values, scores, and status (red/amber/green)

### Dependencies

Key Python packages: `scikit-learn` (IsolationForest), `shap` (feature importance), `pandas` (data manipulation), `azure-data-tables`, `azure-storage-queue`.

---

## AI Outliers · .NET Integration
_chunk 410 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

### API Client

This is used in Store/Cashier profiles, Top Outliers Dashboard, and SecureAI Work Item Generation.

`SecureAiOutlierAnalysisApiClient` builds URLs and calls the Python API. Uses Refit via `IAiOutlierApi` interface. Configured via:

- `SecureAI.OutlierAnalysisUrl` — Python API base URL
- `SecureAI.OutlierAnalysisApiRequestTimeoutSeconds` — default 120s

### SecureAI Work Item Generator

Runs every 15 minutes as a HATR Durable Functions orchestration. See `work-item-generation.md` for the general work item pipeline — the SecureAI generator follows the same 3-step pattern with specialised processors.

**Key files:**

| File | Purpose |
|---|---|
| `Sources/Hatr/.../SecureAiWorkItemGenerator/SecureAiWorkItemGeneratorTask.cs` | HATR orchestration (task ID: `438c17ef-...`) |
| `Sources/Hatr/.../SecureAiWorkItemGenerator/SecureAiWorkItemGeneratorActivity.cs` | Activity — instantiates generator + API client |
| `Sources/Core/Core/Instant Analytics/SecureAI/SecureAiWorkItemGenerator.cs` | Main orchestrator |
| `Sources/Core/Core/Instant Analytics/SecureAI/SecureAiDefinitionRequestProcessor.cs` | Definition-level: validates metrics, queues deaggregation |
| `Sources/Core/Core/Instant Analytics/SecureAI/SecureAiDeaggregationProcessor.cs` | Row-level: calls Python API, creates work items |

#### Database Tables

In addition to the standard `workview.Workview` table, SecureAI populates:

| Table | Purpose |
|---|---|
| `workview.WorkItemPopulationOutlierResults` | Summary per outlier (rank, score, labels) |
| `workview.WorkItemPopulationOutlierReasons` | Top metrics per outlier (SHAP values, status) |

---

## AI Outliers · Configuration
_chunk 411 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

All flags and config items are managed through the Configuration Item page in Control Panel. See [AI Outliers - Configuration](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474741833731) for the full list.

Key items:

| Config Item | Default | Purpose |
|---|---|---|
| `SecureAI.OutlierBoundaryPercent` | 1% | Amber threshold; red = 1/10 of amber |
| `SecureAI.OutlierStatuses` | `red,amber` | Which statuses count as outliers |
| `SecureAI.MaxTotalWorkItems` | 100 | Max work items per definition |
| `SecureAI.UseShapBoundaryForOutlierAnalysis` | false | Use SHAP values for colouring |
| `Profile.OutlierLocationHierarchyPartitionKey` | `LocationHierarchy2` | Hierarchy level for partitioning |
| `Feature.OutliersAi.UsePythonApi` | false | Use Python API vs deprecated service |

---

## AI Outliers · Local Development
_chunk 412 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/ai-outliers.md_

```bash
# Start API with Azurite storage emulator
cd Sources/PythonApi/ai_outliers
docker-compose up

# Or natively
uvicorn app:app --port 8080

# Run job processor
python run_job.py
```

Web UI for reviewing results: `http://localhost:8080/view/local/{clientid}/{keysetid}`

See `Sources/PythonApi/ai_outliers/README.md` for full setup instructions.

## Cache · Overview
_chunk 413 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/cache.md_

Caching in the Secure Platform is distributed by default. Each app node holds a local in-process cache for speed; invalidations are fanned out to every other node so tenants never see stale data across a multi-node deployment.

The main caching mechanism is the Core cache — reached through `Director.ClientCache` (per-tenant) and `SystemCache` (cross-tenant). A second, newer pattern (`ICache`) is used by some of the C# services under `Sources/Incident/`; it sits alongside the Core cache and serves different call sites.

---

## Cache · Architecture
_chunk 414 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/cache.md_

```
            +------------------------+
Caller ---> | ICacheService (local)  |  ConcurrentDictionary per ClientID
            +-----------+------------+
                        |
                        | purge/upsert broadcast
                        v
              +---------+----------+
              |  Redis pub/sub     |  channel: "CacheService"
              |  (Azure)           |
              +---------+----------+
                        |
            +-----------+------------+
            |  peer nodes receive    |
            |  apply locally         |
            +------------------------+
```

Local reads never hit the network. Writes (`Upsert`, `PurgeByKey`, `PurgeByCategory`) are applied locally and then broadcast. Non-Azure deployments fall back to HTTP POSTs to a configured list of farm nodes instead of Redis pub/sub.

---

## Cache · Core cache
_chunk 415 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/cache.md_

The Core cache is the primary caching mechanism across the platform. It comes in two flavours depending on whether the cached data is tenant-scoped or system-wide.

**Key files:**
- `Sources/Core/Core/Cache/ICacheService.cs` — public interface
- `Sources/Core/Core/Cache/CacheService.cs` — base implementation
- `Sources/Core/Core/Cache/ClientCacheService.cs` — per-tenant variant (rejects ClientID 0)
- `Sources/Core/Core/Cache/SystemCacheService.cs` — system-wide variant
- `Sources/Core/Core/Cache/SystemCache.cs` — static wrapper around the singleton `SystemCacheService`
- `Sources/Core/Core/Cache/Model/CacheValue.cs` — value + categories wrapper
- `Sources/Core/Core/Cache/Model/CacheRequest.cs` — cross-node message payload
- `Sources/Core/Core/Data Service Host/RequestHandlers/CacheRequestHandler.cs` — `/cache/` diagnostic endpoints

### Client vs system scope

| Entry point | Scope | When to use |
|---|---|---|
| `Director.ClientCache` | Per-tenant | Anything tenant-specific: user permissions, client config, per-client search results |
| `Director.SystemCache` / `SystemCache` (static) | Cross-tenant | Platform-wide data: connection metadata, DB names, shared lookups |

`ClientCacheService` explicitly refuses a ClientID of 0 (throws with *"Cannot use client ID 0 with ClientCacheService. Use SystemCacheService instead."*), which is how the two stay separate at runtime. Internally both are backed by the same `ConcurrentDictionary<int, ConcurrentDictionary<string, CacheValue>>` machinery — client 0 is reserved for `SystemCache`.

### Usage

```csharp
// per-tenant
Director.ClientCache.Upsert(SmartTrackCacheId, resultsToCache);
var cached = Director.ClientCache.Get<IEnumerable<SmartTrackRepoFile>>(SmartTrackCacheId);
Director.ClientCache.PurgeByKey("SmartTrackResults");
Director.ClientCache.PurgeByCategory("User_Permissions");

// system-wide (via director)
Director.SystemCache.PurgeAll();

// system-wide (static, no director in scope)
SystemCache.Upsert("MaterialisedReferenceDbName", name);
if (SystemCache.TryGet<string>("MaterialisedReferenceDbName", out var cachedName)) { ... }
```

### TTL

TTL is opt-in via `RegisterTtlForKey(key, TimeSpan)`. A `System.Timers.Timer` runs once a minute and evicts expired entries locally; peer nodes expire the same entry independently (clocks must be broadly in sync).

### Invalidation

Four invalidation modes, in order of how targeted they are:

| Method | Scope |
|---|---|
| `PurgeByKey(params string[] keys)` | One or more specific keys in this cache |
| `PurgeByCategory(params string[] categories)` | All keys tagged with a category |
| `PurgeAll()` | Every key in this cache (per-tenant for `ClientCache`, everything for `SystemCache`), audit-logged |
| `Nuke()` | Every tenant's `ClientCache`. Requires the `CachePurge.NukeAuthenticationKey` secret |

Categories are the primary hook for bulk drops — anything tagged e.g. `User_Permissions` gets purged in one call.

### Cross-node broadcast

Two transports, picked at startup based on the `RunningInAzure` config flag:

- **Redis pub/sub (Azure)** — every mutating call publishes a `CacheRequest` message to the `CacheService` channel. Subscribers on every node apply the same mutation locally. Messages carry `OriginalProcessId` so the sender ignores its own echo.
- **HTTP farm (non-Azure)** — the sender posts to every node listed in `CachePurge.MembersList`. Requests are signed with `CachePurge.AuthenticationKey` and have a `CacheService.TimeoutInSeconds` request timeout.

Broadcasts happen on a background thread so the caller isn't blocked waiting for peers to acknowledge.

### Configuration

Connection strings and farm membership live in the Configuration database (see `databases/sql-mi.md`) and are served via `IGlobalConfigurationService`:

| Config key | Purpose |
|---|---|
| `RunningInAzure` | Toggles Redis pub/sub vs HTTP farm transport |
| `CachePurge.MembersList` | Comma-separated peer node URLs (non-Azure) |
| `CachePurge.AuthenticationKey` | HMAC secret for peer POSTs |
| `CachePurge.NukeAuthenticationKey` | Secret required for `Nuke()` |
| `CacheService.TimeoutInSeconds` | Peer request timeout |

---

## Cache · ICache (Incident C# services)
_chunk 416 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/cache.md_

Some of the newer C# services under `Sources/Incident/` use `ICache`, an async, callback-based cache fronted directly by Redis. It does not replace the Core cache — it's a parallel abstraction used in those specific services.

**Key files:**
- `Sources/Incident/ApprissRetail.Secure.Common/Caching/ICache.cs` — interface
- `Sources/Incident/ApprissRetail.Secure.Common/Caching/Implementation/Redis/RedisCache.cs` — Redis implementation
- `Sources/Incident/ApprissRetail.Secure.Common/Caching/CacheOptions.cs` — configuration

The interface is callback-based rather than explicit get/set. If the key is missing, the supplied factory runs and its result is cached:

```csharp
var orcProfile = await cache.ObjectGetAsync(
    onCacheMiss: () => orcClient.LoadProfileAsync(userId),
    keyHierarchy: new[] { "orc", "profile", userId.ToString() });
```

`keyHierarchy` is joined with colons and prefixed with `"{ApplicationName}:{EnvironmentName}:{PaddedClientID}"` from `CacheOptions` — that's what isolates tenants and environments on a shared Redis instance. Values are serialized with Newtonsoft.Json; the sentinel `$$NULL$$` distinguishes a cached null from a miss.

Configuration example (Control Panel `appsettings.json`):

```json
"EnableRedis": true,
"Redis": "127.0.0.1:6380, abortConnect=false"
```

> **Known limitation.** `RedisCache` currently hard-codes ClientID to 1. Multi-tenant support here is still in progress; in practice these services run in tenant-scoped contexts today.

---

## Cache · Related
_chunk 417 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/cache.md_

- Control Panel has a cache admin UI at `Sources/UI/Components/src/_react/src/apps/control-panel/pages/cache/` for inspection and manual purges.
- Yarp reloads its routing tables via the Redis `CacheService` channel — see `docs/04-development/yarp.md`.
- For Square Hierarchy work, clearing the cache after flipping `Feature.SquareHierarchies.*` flags is required — see `features/hierarchy-generation.md`.

## Control Panel · Overview
_chunk 418 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

The Control Panel is the internal admin tool for configuring tenants on the Secure platform. It is not user-facing — only Appriss Retail staff (engineers, delivery, support, product) use it.

**Source:** `Sources/UI/ControlPanel/`

---

## Control Panel · Hosting Model
_chunk 419 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

Control Panel is an **ASP.NET Core** backend with a **React SPA** frontend.

Yarp routes `/control` to the Control Panel service (port 7096 locally via Kestrel TLS).

### How it works

1. A Razor Page at `/` (`Pages/React/Index.razor.cshtml`) renders a shell HTML page with three mount points.
2. The React bundle (`_react/dist/home.js`) is loaded via a `<script>` tag. The filename is content-hashed in production; the Razor page reads `manifest.json` to resolve it.
3. React Router (v6, hash-based) handles all navigation within the React SPA.
4. 26 API controllers under `[Route("api/[controller]")]` provide the backend.

### Three React mount points

| DOM id | Component | Purpose |
|--------|-----------|---------|
| `react-app-root` | `RouterProvider` (all page routes) | Main content area |
| `react-sidebar-root` | `ControlPanelSidebar` | Left nav — environment selector + page links |
| `react-charms-root` | `ControlPanelCharms` | Header — theme switcher, user menu |

> **Note:** A handful of `.razor` files remain under `Pages/` (CCTV, PermissionsReview, CompleteReasons) but are excluded from compilation — they are kept as reference during the React migration.

---

## Control Panel · Authentication and Authorisation
_chunk 420 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

**Production:** Azure Active Directory via OpenID Connect.

**Development:** `DevAuthHandler` auto-authenticates as "Developer" with the `EngineeringManagers` role. No login required locally.

### Roles

| Role | Typical access |
|------|---------------|
| `Engineers` | Full engineering access |
| `EngineeringManagers` | Full access + destructive operations |
| `DeliveryManagers` | Client config, feature flags |
| `Delivery` | Client config (read-heavy) |
| `SolutionExpert` | Feature flags, client attributes |
| `Infrastructure` | Cache, Yarp, monitoring |
| `DataScience` | Snowflake cost, AI outliers |
| `SupportL1` / `SupportL2` | Logs, HATR, service alerts |
| `Csms` | Client-facing features |
| `ProductManagers` | Feature flags, config |
| `Marketing` | Logon news |

---

## Control Panel · Data Access
_chunk 421 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

### ConfigurationContext

Global configuration database (SQL Server). Contains clients, connection strings, config items.

### MultiClientDbContext

Scoped service that creates per-client database contexts on construction. Three contexts per enabled client:

| Context | Connection name | Providers | Purpose |
|---------|----------------|-----------|---------|
| `PlatformDbContext` | `application-direct` | SQL Server | App data (users, searches, incidents) |
| `MetricDbContext` | `metricbase-direct` | SQL Server, Greenplum | Analytics metrics |
| `ArdmSecureDbContext` | `securereferencedata-direct` | Greenplum, Snowflake | ARDM reference data |

### SnowflakeDbContextFactory

Lightweight factory for Snowflake-only queries. Provides global context (for `SNOWFLAKE.ACCOUNT_USAGE`) and per-client contexts (via `pos-data` connection strings).

---

## Control Panel · Backend Patterns
_chunk 422 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

### Controller → Service

```
[Route("api/[controller]")] Controller
    → Scoped Service (Data/)
        → MultiClientDbContext / ConfigurationContext / SnowflakeDbContextFactory
```

All responses wrapped in `JsonActionResult` with `{ success, data }` shape. Role checks at the top of each action method.

### Response structure

`JsonActionResult` wraps in `ResultBag`, so the full response is:

```json
{
  "success": true,
  "data": {
    "success": true,
    "data": [ ... ]
  }
}
```

React services receive the outer object; actual data is at `response.data.data`.

---

## Control Panel · React Frontend
_chunk 423 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

### Key directories

```
_react/src/
├── apps/control-panel/
│   ├── index.js          Router config + mount points
│   ├── pages/            41+ page components
│   ├── services/         API service layer
│   └── hooks/            Custom hooks
├── shared/               CP-specific components (pickers, sidebar)
└── constants.js          String constants
```

### Path aliases

| Alias | Resolves to |
|-------|-------------|
| `@shared` | Shared component library (`UI/Components/src/_react/src/shared`) |
| `@cpshared` | Control Panel components (`_react/src/shared`) |
| `@constants` | `_react/src/constants.js` |

### Build

```bash
cd Sources/UI/ControlPanel/_react
npm run dev     # watch mode
npm run build   # production with content hashing
```

---

## Control Panel · Further Reading
_chunk 424 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/control-panel.md_

Detailed docs live alongside the source code:

- **Architecture deep-dive:** `Sources/UI/ControlPanel/docs/architecture.md`
- **How to add a React page:** `Sources/UI/ControlPanel/docs/adding-a-react-page.md`

## Data Model & Ingestion · Overview
_chunk 425 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/data-model.md_

Understanding how data gets into the platform — and what shape it's in when it arrives — is essential background for any work that touches search, reporting, or HATR (high availability task runner).

## Data Model & Ingestion · The ARDM
_chunk 426 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/data-model.md_

The **Appriss Retail Data Model (ARDM)** is the central analytics database. It is the schema that the application queries when an analyst runs a search. Every data area in the search builder (POS transactions, returns, employee data, inventory, etc.) corresponds to tables in the ARDM.

Key characteristics:

- **Multi-tenant at schema level** — each client has their own ARDM schema (e.g. `client_1`, `client_42`). There is no cross-contamination of data between tenants at the database level.
- **Normalised common model** — regardless of what POS system or data format a client uses, their data arrives in the ARDM in a consistent structure. This is what makes writing a single search work across all clients.
- **Snowflake** in newer deployments. Older environments still use Greenplum (PostgreSQL) — you will encounter both.

## Data Model & Ingestion · The legacy CRDM
_chunk 427 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/data-model.md_

You will see references to the **CRDM (Common Retail Data Model)** in older Confluence pages and the 5.x versioned documentation. CRDM was the predecessor to ARDM build on MS SQL Server. The ARDM is effectively the modernised, cloud-native successor. When you see CRDM in older code, it refers to the same conceptual thing but the legacy schema version.

## Data Model & Ingestion · How data gets in: the pipeline
_chunk 428 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/data-model.md_

### Legacy path (PyARDM / SDL)

The original ingestion mechanism. A Python-based tool called **PyARDM** runs transforms over client data into the ARDM schema. Python code defines the mapping from raw client format to ARDM tables.

This path is being retired. Some clients are still on it. You may encounter PyARDM code and jobs but should not be extending it.

### New path (SnowTime)

**SnowTime** is the replacement. A six-step Azure/Snowflake pipeline:

```
1. Landing      →  Azure Blob (raw encrypted files from client)
2. Processor    →  Azure Function decrypts (PGP) and validates
3. Ingest Area  →  Azure Blob as Snowflake External Stage
4. Ingest       →  Snowflake COPY INTO (raw → Snowflake tables)
5. Transform    →  DBT Core (Snowflake → ARDM schema)
6. Post-process →  Merge, dedup, downstream triggers
```

SnowTime is designed so that basic SQL knowledge is sufficient to onboard a new customer — you do not need to be a Python engineer to write a data transformation. DBT models are SQL with Jinja templating.

Supported formats: CSV, JSON, XML, Avro, Parquet, raw binary.

Key principles:
- **Never lose data** — the landing area is immutable; files are only moved, never deleted, until explicitly retired.
- **Respect arrival order** — if a file arrives late or is redelivered, the pipeline handles it correctly.
- **Fault-tolerant** — individual step failures do not corrupt downstream state.
- **70% unit test coverage minimum** for Azure Function code.

[SnowTime Design & Architecture](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/476697231374/Project+SnowTime+-+Design+and+Architecture)

### Other ingestion paths

- **sFTP + AR Gateway** — For clients using REST APIs, Kafka topics, or queues instead of flat files. The AR Gateway normalises these into the standard landing format.
- **Shopify** — Dedicated integration for Shopify-based ecommerce clients.
- **Facteus** — Third-party data enrichment.
- **ARWS** — Internal Appriss Retail Web Service integration.

## Data Model & Ingestion · Data areas
_chunk 429 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/data-model.md_

A "data area" in Secure is what analysts select when building a search. Each data area corresponds to one or more ARDM tables:

- POS Exceptions — till transactions
- SCO Exceptions — self-checkout
- Online Exceptions — ecommerce
- Claims Exceptions — returns/refunds (Engage)
- Curbside, DSD, Cash Over/Short — specialist transaction types
- Employee data, Location, SKU — reference data areas

When a new client is onboarded, their reference data (stores, employees, products) is loaded first, before transaction data, because the transaction records need to reference valid locations and employees.

## Data Model & Ingestion · Database housekeeping
_chunk 430 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/data-model.md_

Old data is not kept forever.  Database Housekeeping policies define retention periods per data type, which are contractually agreed with each retailer. Out-of-range data is cleaned on a maintenance schedule (Maintenance Type 1 jobs in the job system).

---

*Back: [Database Architecture](databases.md) · Next: [Environment Setup](../04-development/environment-setup.md)*

## Database Architecture · Overview
_chunk 431 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/databases.md_

This page gives the high-level picture of how Secure's databases fit together. For the details of each technology, see the linked sub-pages.

For how data *gets into* the platform (ingestion pipelines, SnowTime, ARDM schema details), see [Data Model & Ingestion](data-model.md).

---

## Database Architecture · Overview
_chunk 432 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/databases.md_

Secure uses two broad categories of database:

1. **Application databases (SQL Server on Azure SQL Managed Instance)** — store configuration, investigations, work items, generated metrics metadata, membership, incidents, and all operational platform state. Each tenant has its own pair of databases (platform + reference) on a shared SQL MI. A single shared configuration database ties everything together.
2. **Analytics databases (Snowflake, legacy Greenplum)** — store the ARDM (Appriss Retail Data Model) — the normalised POS and retail data that powers search. Each tenant has its own ARDM schema *and* a per-client Secure schema for data that is joined to ARDM at query time.

| Database | Technology | Purpose |
|---|---|---|
| **Platform** | SQL Server (Azure SQL MI) | Core application data — investigations, work items, SSO, dashboards, notifications |
| **Configuration** | SQL Server | Tenant metadata, connection strings, feature flags, logs, service state |
| **ARDM** | Snowflake (active) / Greenplum (legacy) | Analytics — POS transactions, inventory, ecommerce. Migration to Snowflake in-flight. |

Most user-facing functionality touches both categories. A search joins ARDM tables (POS transactions, locations, employees) to per-client Secure-owned data (metric outputs, investigation transaction links, enumeration lookups), while the saved search definition, work items generated from the results, and any resulting investigation live in the platform database.

Access to databases follows the same environment split as the rest of the platform. See [Environments — Database Access](environments.md#database-access) for rules (notably, production requires the jump server).

---

## Database Architecture · Database types
_chunk 433 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/databases.md_

| Technology | Role | Details |
|---|---|---|
| [SQL Managed Instance](databases/sql-mi.md) | Application state — configuration DB + per-tenant platform/reference DBs | Naming conventions, schemas (secure, factboard, workview, membership, …), client attributes |
| [Snowflake](databases/snowflake.md) | Active analytics warehouse — ARDM + per-client Secure schema | `ARP_{SLOT}` databases, ARDM versions, `C{id}_{abbr}` Secure schemas, connecting locally |
| [Greenplum (legacy)](databases/greenplum.md) | Outgoing analytics warehouse | Cluster/database/schema mapping, `secure_{clientId}` schemas |
| [Lunar](databases/lunar.md) | The installer/seeder that provisions all of the above | Providers, seed layering, EF Core migrations, Programmability |
| [Other data stores](databases/other.md) | Feature-specific stores | AI Outliers Azure Table Storage, ORC Azure AI Search + `TenantSearchInfo` |
| [Azure Key Vault](databases/key-vault.md) | Secrets store referenced by `$KV(...)` tokens | Vault naming, secret naming convention, `KeyVaultResolver`, local user-secrets |

---

## Database Architecture · Multi-Tenancy and Connection String Resolution
_chunk 434 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/databases.md_

The platform uses the single shared **Configuration database** as the bootstrap point. It contains the `arp.Clients` table (all tenant metadata) and `arp.ConnectionStrings` table (per-client connection string mappings). At runtime, `GlobalConfigurationService` loads the client list and connection strings from this shared database, and `ConnectionsService` resolves per-client connections by ClientID + connection name.

### Isolation model

| Database | Isolation | How it works |
|---|---|---|
| **Configuration** | Shared, single instance | One database for all clients. Contains client list, connection strings, global config, logs. |
| **Platform** | Per-client database | Each client has its own Platform DB. Resolved via `application-direct` connection name per ClientID. |
| **ARDM (Snowflake)** | Schema-per-tenant | See [Snowflake](databases/snowflake.md). |
| **ARDM (Greenplum)** | Schema-per-tenant | See [Greenplum](databases/greenplum.md). |

### Connection string resolution flow

```
Configuration DB (shared)
  ├── arp.Clients — all tenant metadata (ClientID, Name, Secret, Abbreviation, DatabaseServerID)
  └── arp.ConnectionStrings — per-client connection name → connection string mappings
        ↓
GlobalConfigurationService loads client list on startup
        ↓
User authenticates → Director.SetClientID(clientID, hash)
        ↓
ConnectionsService.GetClientConnectionInfo(connectionName, director)
  → looks up ConnectionStrings[clientID][connectionName]
  → returns per-client connection string
        ↓
Per-client database access (Platform DB, Metric DB, ARDM, etc.)
```

### Key connection names

| Connection name | Target Database | MSSQL / GP / Snowflake | Per-client? |
|---|---|---|---|
| `global-configuration` | Configuration DB | MSSQL | No |
| `application-direct` | Platform DB | MSSQL | Yes |
| `pos-data` | POS transaction data | Greenplum / Snowflake | Yes |
| `securereferencedata-direct` | ARDM reference data | Greenplum / Snowflake | Yes |
| `securereferencedata-direct-mssql` | Replicated ARDM reference data | MSSQL | Yes |
| `membership-direct` | User membership | MSSQL | Yes |
| `configuration` | Per-client config items | MSSQL | Yes |

Defined in `Sources/Core/Core/Data/Contract/CoreConnections.cs`.

---

## Database Architecture · Application Behaviour to Database Mapping
_chunk 435 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/databases.md_

Understanding what end users do helps clarify which tables and data are involved.

### Search (the core interaction)

The primary user interaction in Secure is **search**. Searches are the building block for everything — reports, metrics, work items, and investigations all start with a search.

| User action | Data involved |
|---|---|
| Build and run a search | Queries ARDM tables, joined to the per-client Secure warehouse schema for metrics, user scoping, enumerations |
| View aggregated results | ARDM data, aggregated at query time |
| Drill down to a receipt | ARDM transaction-level detail |
| Navigate to a store or cashier profile | ARDM reference data (locations, employees) |
| Save a search | Search definition persisted to SQL MI (`secure` / module schema in the platform DB) |
| Generate work items from results | Rows created in `workview` (platform DB), referencing ARDM transaction IDs |
| Open an investigation | Record created in `factboard` (platform DB); referenced transactions written to the per-client Secure warehouse schema |

### Pre-defined and saved searches

The platform ships with pre-defined searches (configured per client) and allows users to save their own. Both are stored as database-backed definitions in the platform DB. When executed, they generate queries against the ARDM joined with the per-client Secure warehouse schema.

---

## Database Architecture · Data Dictionary
_chunk 436 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/databases.md_

A comprehensive data dictionary covering all tables — tenant platform databases, the configuration database, the per-client Secure warehouse schemas, and the ARDM — is actively being developed. It will serve as the authoritative reference for column-level detail, relationships, and deprecation status.

Until the data dictionary is complete, the best way to understand a specific table is to:

1. Check the appropriate schema in a non-production tenant database (e.g. Astromart in local dev for SQL MI, or `ARP_QA.C001_AMT` in Snowflake)
2. Review the relevant application code — the Director/Service/DAL layers map closely to the underlying tables
3. Ask the engineering team if the table's purpose is unclear

---

*Back: [Technology Stack](technology-stack.md) · Next: [Data Model & Ingestion](data-model.md)*

## Azure Durable Task Scheduler · What Is It?
_chunk 437 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

The Azure Durable Task Scheduler is a fully managed, purpose-built backend-as-a-service for [Durable Functions](https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler) and the Durable Task SDKs. It replaces the traditional "bring your own" (BYO) storage providers (Azure Storage, Netherite, MSSQL) with a dedicated, optimised scheduling and state management service.

Instead of your Function App polling Azure Storage queues and table storage for orchestration state, the Durable Task Scheduler runs as a separate Azure resource (`Microsoft.DurableTask/scheduler`) with its own dedicated compute and memory. Your app connects to it over a TLS-secured gRPC connection (endpoint format: `{scheduler-name}.{region}.durabletask.io`), and work items are **pushed** to your app rather than polled for.

## Azure Durable Task Scheduler · How It Works
_chunk 438 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

1. **Scheduler Resource** -- You provision a scheduler instance via Azure Resource Manager. Each instance has dedicated compute and memory for dispatching work items and storing orchestration history.
2. **Task Hubs** -- Within a scheduler you create one or more task hubs. A task hub is a logical container that isolates orchestration and entity state. Multiple apps can share one scheduler, each using its own task hub.
3. **Push-Based Work Distribution** -- The scheduler streams orchestrator, activity, and entity work items to your app over gRPC. This eliminates the queue-polling overhead of the Azure Storage provider and reduces end-to-end latency.
4. **Internal State Management** -- State is managed internally by the scheduler using a combination of in-memory (short-lived) and persistent storage (recovery and queries). No separate storage account is needed for orchestration state.
5. **Managed Identity Authentication** -- Apps authenticate to the scheduler using managed identity (user-assigned recommended). Connection-string-with-key authentication is not supported.
6. **Dashboard** -- Every scheduler gets an out-of-the-box monitoring dashboard for viewing orchestration instances, filtering by status, drilling into sub-orchestrations, and performing management operations (pause, terminate, restart).

## Azure Durable Task Scheduler · Advantages Over Azure Storage Hosted
_chunk 439 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

| Concern | Azure Storage Provider | Durable Task Scheduler |
|---|---|---|
| **Throughput** | Limited by storage queue throughput and polling intervals | Highest throughput of all backends; push-based streaming removes polling overhead |
| **Latency** | Queue polling introduces latency (configurable but inherent) | Sub-second dispatch via gRPC push model |
| **Resource Consumption** | Function App CPU and memory used for partition management, queue polling, and state store interactions | Offloaded to the managed scheduler; reduced CPU/memory on Function App instances |
| **State Storage** | You manage a storage account (queues, tables, blobs); costs accrue per transaction | Internal to the scheduler; no separate storage account to manage or pay for |
| **Observability** | Limited; requires Application Insights queries or custom tooling | Built-in dashboard with filtering, drill-down, and management operations |
| **Scaling** | Storage account and Function App scale together; partition management is in-process | Scheduler scales independently of the app; multiple apps can share one scheduler |
| **Fault Isolation** | Storage failures can cascade into Function App failures | Operational separation; scheduler failures do not directly crash your app |
| **Maintenance** | You manage storage account lifecycle, networking, key rotation | Fully managed service with streamlined support and diagnostics |
| **Autopurge** | Manual or custom cleanup of completed orchestrations | Built-in configurable autopurge retention policies |

## Azure Durable Task Scheduler · Production Limitation: No Private Networking Support
_chunk 440 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

> **The Durable Task Scheduler does not currently support private endpoints or virtual network (VNet) integration.**

Apps connect to the scheduler over a **public gRPC endpoint** (`*.durabletask.io`). There is no way to place the scheduler behind a private endpoint or route traffic through a VNet.

**What this means for us:** Our production environments require virtual networking. All traffic between services must stay within our VNet or traverse private endpoints. Until Microsoft adds private networking support to the Durable Task Scheduler, **it must not be used in any environment where VNet isolation is required**. This includes our production and staging environments.

The scheduler is suitable for:
- Local development (via the emulator)
- Proof-of-concept and performance benchmarking

Monitor the [Azure updates page](https://azure.microsoft.com/updates/) and the [Durable Task Scheduler documentation](https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler) for private networking announcements.

## Azure Durable Task Scheduler · Durable Task Scheduler Dashboard
_chunk 441 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

Every scheduler resource comes with a built-in web dashboard hosted at `dashboard.durabletask.io`. The dashboard provides real-time visibility into all orchestration and entity instances running within a task hub, without needing Application Insights queries or custom tooling.

<img src="durable-functions-dashboard.png" alt="Durable Task Scheduler Dashboard showing orchestration instances in the DevSystemTasks task hub" width="700" />

### What the Dashboard Shows

- **Summary Cards** -- At-a-glance counts for All, Completed, Failed, Running, and Pending orchestrations.
- **Orchestration List** -- A sortable, filterable table showing each orchestration's ID, name, last updated timestamp, duration, and runtime status.
- **Instance Detail** -- Click any orchestration ID to drill into its execution history, see sub-orchestrations and activity calls, inspect inputs/outputs, and view error details for failures.

### Left-Hand Navigation

| Section | Purpose |
|---|---|
| **Orchestrations** | View and manage all orchestration instances (the main view shown above) |
| **Entities** | View and manage durable entity instances |
| **Schedules** | View scheduled orchestrations and timers |
| **Workers** | See connected worker apps and their status |

### Management Operations

From the dashboard you can perform actions on selected orchestrations:

- **Start Orchestration** -- Trigger a new orchestration instance directly from the UI.
- **Resume / Suspend** -- Pause or resume running orchestrations.
- **Restart** -- Restart a completed or failed orchestration.
- **Terminate** -- Force-stop a running orchestration.
- **Purge** -- Delete orchestration history and state.
- **Auto Refresh** -- Toggle automatic polling to keep the view current.

### Access Control

Dashboard access is secured via identity and role-based access control (RBAC). You must have the appropriate role assigned to your developer identity (email) on the scheduler or task hub resource. The relevant roles are:

| Role | Access Level |
|---|---|
| `Durable Task Data Contributor` | Full read/write access to orchestration data and management operations |
| `Durable Task Data Reader` | Read-only access to orchestration and entity data |
| `Durable Task Worker` | Worker-level access for processing orchestrations (not typically used for dashboard) |

Access can also be filtered by IP, but it is not possible to filter traffic from a VNet. Private endpoint and VNet integration are not currently supported.    

### Dashboard URL Format

The dashboard URL follows this pattern:

```
https://dashboard.durabletask.io/subscriptions/{subscription-id}/schedulers/{scheduler-name}/taskhubs/{taskhub-name}/orchestrations
```

For the local emulator, the dashboard is available at `http://localhost:8082`.

## Azure Durable Task Scheduler · Hosting Configuration in Isolated Functions:
_chunk 442 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

In the .NET isolated worker model, the storage provider (Azure Storage vs. Durable Task Scheduler) is configured in `host.json`, **not in application code**. The `storageProvider` section of `host.json` determines which backend the Durable Functions extension uses at runtime:

**Azure Storage (current):**

```json
{
  "extensions": {
    "durableTask": {
      "hubName": "MyTaskHub",
      "storageProvider": {
        "type": "AzureStorage",
        "connectionStringName": "AzureWebJobsStorage"
      }
    }
  }
}
```

**Durable Task Scheduler:**

```json
{
  "extensions": {
    "durableTask": {
      "hubName": "%TASKHUB_NAME%",
      "storageProvider": {
        "type": "azureManaged",
        "connectionStringName": "DURABLE_TASK_SCHEDULER_CONNECTION_STRING"
      }
    }
  }
}
```

**Why this matters:** You cannot programmatically switch the storage provider at runtime in isolated Functions. The `host.json` file is read at startup by the Functions host before your application code runs. There is no API or startup hook to override the `storageProvider` configuration from within the isolated worker process.

This means **the deployment pipeline must be responsible for setting the correct `host.json` values** for each environment. In practice:

1. The `host.json` checked into source control should target the **local emulator** (`azureManaged` with `Endpoint=http://localhost:8080;Authentication=None`).
2. The deployment pipeline transforms `host.json` (or replaces environment-specific app settings) to point at the correct backend for each target environment.
3. For environments still on Azure Storage, the pipeline sets `type: AzureStorage`.
4. For environments migrated to Durable Task Scheduler, the pipeline sets `type: azureManaged` with the appropriate connection string and task hub name.

For C# isolated worker projects, the Durable Task Scheduler support is provided by the [Microsoft.Azure.Functions.Worker.Extensions.DurableTask.AzureManaged](https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker.Extensions.DurableTask.AzureManaged) NuGet package.

# Migration Plan

Since orchestration data **cannot be migrated** between storage providers, a clean cutover is not possible for in-flight orchestrations. Instead, we will need to use a dual-running strategy where the old Azure Storage backend drains while the new Durable Task Scheduler starts up.

### Phase 1: Preparation

1. **Provision the Durable Task Scheduler** resource and task hub in the target Azure region (same region as the Function App). This should be done through Terraform using the **AzAPI provider** (not AzureRM), which supports `Microsoft.DurableTask` resources via ARM API directly.

   **Scheduler resource:**

   ```terraform
   resource "azapi_resource" "scheduler" {
     type      = "Microsoft.DurableTask/schedulers@2026-02-01"
     name      = "my-scheduler"
     parent_id = azurerm_resource_group.example.id
     location  = "eastus"

     tags = {
       environment = "production"
     }

     body = {
       properties = {
         ipAllowlist         = ["0.0.0.0/0"]
         publicNetworkAccess = "Enabled"
         sku = {
           name     = "Consumption"  # or "Dedicated"
           capacity = 1              # only relevant for Dedicated SKU
         }
       }
     }
   }
   ```

   **Task Hub resource (child of scheduler):**

   ```terraform
   resource "azapi_resource" "task_hub" {
     type      = "Microsoft.DurableTask/schedulers/taskHubs@2026-02-01"
     name      = "default"
     parent_id = azapi_resource.scheduler.id

     body = {
       properties = {}
     }
   }
   ```

   **Key points:**

   - **Name constraints:** Scheduler and task hub names must be 3--64 characters, alphanumeric and hyphens only (`^[a-zA-Z0-9-]{3,64}$`).
   - **SKUs:** Consumption (up to 10 schedulers per region/subscription) or Dedicated (up to 25, with configurable capacity units for zone redundancy).
   - **`ipAllowlist`** is required -- use `["0.0.0.0/0"]` to allow all, or lock it down to specific CIDRs.

2. **Create a managed identity** (user-assigned) and assign the `Durable Task Data Contributor` RBAC role on the scheduler and task hub. This identity must also be assigned to the Function Apps that will connect to the DTS.
3. **Update the deployment pipeline** to support environment-variable-driven backend selection in `host.json` (see section above).

## Azure Durable Task Scheduler · Hosting Configuration in Isolated Functions: (cont. 2)
_chunk 443 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

4. **Install the DTS NuGet package** (`Microsoft.Azure.Functions.Worker.Extensions.DurableTask.AzureManaged`) in the Function App project. The standard GA extension bundle is sufficient for C# isolated worker projects.
5. **Test locally** using the DTS emulator to verify the app works correctly with the new backend.

### Phase 2: Shadow Deployment (New Orchestrations to DTS)

1. **Deploy a second Function App instance** (or deployment slot) configured to use the Durable Task Scheduler backend. This instance handles **new** orchestration triggers only.
2. **Route new orchestration starts** to the DTS-backed instance. This can be done via:
   - **Feature flag at the caller level:** All HATR orchestrations are started via HTTP POST to the `EnqueueTask` endpoint. The service that calls HATR would check a feature flag to determine which Function App URL to POST to -- the old Azure Storage-backed instance or the new DTS-backed instance. Since the routing decision happens at the caller before the HTTP request is made, this is a simple URL swap with no changes needed inside HATR itself. The feature flag can be toggled gradually (e.g., by tenant, by task type, or as a global switch) to control the rollout.
   - **Traffic splitting at the load balancer or slot level.**
   - **Disabling timer/queue triggers** on the new instance that would pick up old work.
3. The **original Function App instance** (Azure Storage backend) continues processing its existing in-flight orchestrations but **stops accepting new orchestration starts**. No configuration change is needed on the old instance to achieve this -- since all HATR orchestrations are initiated via HTTP POST to `EnqueueTask`, the old instance simply stops receiving new requests once the feature flag routes all callers to the new DTS-backed URL. The only timer trigger on the old instance (`PruneTaskHistory`, daily at midnight) is a maintenance operation that cleans up history, not an orchestration start, so it can safely continue running during the drain period.
4. **Monitoring both backends:** Each backend has its own observability surface. The DTS-backed instance can be monitored via the Durable Task Scheduler dashboard. The Azure Storage-backed instance can be monitored via the Durable Functions HTTP APIs or Azure Storage Explorer. There is no single view across both backends during the transition period.

### Phase 3: Drain the Old Backend

1. **Monitor the Azure Storage task hub** for in-flight orchestrations. Use the Durable Functions HTTP APIs or Azure Storage Explorer to check for running/pending instances.
2. As orchestrations on the old backend **complete naturally**, the load tapers off. Set a target drain period based on your longest-running orchestration.
3. **Do not forcefully terminate** old orchestrations unless they are stuck or failed. Let them complete their natural lifecycle.
4. For **stuck or zombie orchestrations**, use the Durable Functions purge APIs to clean them up after investigation.

### Phase 4: Cutover

1. Once the old Azure Storage task hub has **zero running orchestrations**, decommission the old Function App instance.
2. Update the pipeline so that all environments point exclusively at the Durable Task Scheduler backend.
3. Remove the old Azure Storage task hub resources (queues, tables, blobs) after a grace period.

### Migration Visualisation

```
           Old instance: ========....  (existing work draining)
           New instance: ..========..  (new work ramping up)
           Old instance: ====........  (tail of long-running orchestrations)
           New instance: ....========  (handling all new work)
           Old instance: ............  (drained, decommission)
           New instance: ============  (sole backend)
```

Timelines will vary based on orchestration duration and volume. The key principle is: **never cut off in-flight orchestrations; let them drain naturally on the old backend.**

# Running Locally

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
- [Azurite](https://learn.microsoft.com/azure/storage/common/storage-install-azurite) installed (still needed for `AzureWebJobsStorage` even when using DTS for durable state).

### Step 1: Start the Emulator

Pull and run the DTS emulator Docker image:

```bash
docker pull mcr.microsoft.com/dts/dts-emulator:latest

docker run --name dts-emulator -d -p 8080:8080 -p 8082:8082 mcr.microsoft.com/dts/dts-emulator:latest
```

## Azure Durable Task Scheduler · Hosting Configuration in Isolated Functions: (cont. 3)
_chunk 444 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

Ports:
- **8080** -- gRPC endpoint (your app connects here)
- **8082** -- Dashboard UI (open `http://localhost:8082` in your browser)

The emulator exposes a single task hub named `default`. To create multiple task hubs:

```bash
docker run --name dts-emulator -d -p 8080:8080 -p 8082:8082 \
  -e DTS_TASK_HUB_NAMES=taskhub1,taskhub2 \
  mcr.microsoft.com/dts/dts-emulator:latest
```

> **Note:** The emulator stores all state in memory. Data is lost when the container stops.

### Step 2: Configure host.json

Set the storage provider to `azureManaged` and point at the local emulator:

```json
{
  "version": "2.0",
  "extensionBundle": {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[4.0.0, 5.0.0)"
  },
  "extensions": {
    "durableTask": {
      "hubName": "%TASKHUB_NAME%",
      "storageProvider": {
        "type": "azureManaged",
        "connectionStringName": "DURABLE_TASK_SCHEDULER_CONNECTION_STRING"
      }
    }
  }
}
```

### Step 3: Configure local.settings.json

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
    "DURABLE_TASK_SCHEDULER_CONNECTION_STRING": "Endpoint=http://localhost:8080;Authentication=None",
    "TASKHUB_NAME": "default"
  }
}
```

### Step 4: Start Azurite and Run

1. Start Azurite (needed for the Functions host, not for durable state):
   ```bash
   azurite --silent
   ```
2. Run your Function App as normal:
   ```bash
   func start
   ```
3. Open `http://localhost:8082` to view the DTS dashboard and monitor orchestrations.

### Stopping the Emulator

```bash
docker stop dts-emulator
docker rm dts-emulator
```

## Azure Durable Task Scheduler · References
_chunk 445 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/durable-task-scheduler.md_

- [Durable Task Scheduler Overview](https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler)
- [Quickstart: Configure Durable Functions with DTS](https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/quickstart-durable-task-scheduler)
- [Storage Providers Comparison](https://learn.microsoft.com/azure/azure-functions/durable/durable-functions-storage-providers)
- [DTS Billing](https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler-billing)
- [DTS Dashboard](https://learn.microsoft.com/azure/azure-functions/durable/durable-task-scheduler/durable-task-scheduler-dashboard)
- [Durable Task Scheduler GitHub Samples](https://github.com/Azure-Samples/Durable-Task-Scheduler/)

## Environments · Overview
_chunk 446 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/environments.md_

The platform runs across six environments, each deployed in both **EU** and **US** regions. Internal environments (DEV through QA) use the `arinternal.net` domain. Customer-facing environments (Staging and Production) use `apprissretailcloud.com`.

## Environments · Environment Summary
_chunk 447 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/environments.md_

| Environment | Visibility | Purpose |
|---|---|---|
| **DEV** | Internal | Short-lived deployments for testing custom branches before they merge. |
| **CICD** | Internal | Auto-deployed on every merge to `main`. Always reflects the latest state of the main branch. |
| **SHOWCASE** | Internal | Long-running custom branch deployments. Use this to demo a feature under development to stakeholders without merging. |
| **QA** | Internal | The QA team's primary environment — manual testing and automated test runs both target this. |
| **Staging** | Customer-facing | Pre-production. Also referred to as **Test**. Accessible to customers for UAT. Used for L2 approvals and release sign-off. |
| **Production** | Customer-facing | Live. Real customer data. Access is restricted and requires justification. |

## Environments · Control Panel URLs
_chunk 448 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/environments.md_

| Environment | EU | US |
|---|---|---|
| DEV | https://eudev.arinternal.net/control | https://usdev.arinternal.net/control |
| CICD | https://eucicd.arinternal.net/control | https://uscicd.arinternal.net/control |
| Showcase | https://eushowcase.arinternal.net/control | https://usshowcase.arinternal.net/control |
| QA | https://euqa.arinternal.net/control | https://usqa.arinternal.net/control |
| **Staging** | https://eustaging.apprissretailcloud.com/control | https://usstaging.apprissretailcloud.com/control |
| **Production** | https://euprod.apprissretailcloud.com/control | https://usprod.apprissretailcloud.com/control |

## Environments · Signing In
_chunk 449 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/environments.md_

You can sign into the Control Panel and click a customer logo to jump directly into their environment. If you are on the login page for a client, you can also ALT-Click the Appriss retail logo to log in via SSO.

## Environments · Database Access
_chunk 450 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/environments.md_

Databases are partitioned the same way as the app environments: one set of tenant databases (plus a shared configuration database) per environment, per region. See [Database Architecture](databases.md) for how they're structured.

Access rules:

- **Non-production** (Dev, CICD, Showcase, QA) — accessible from your local machine while on the VPN.
- **Production and Staging** — all access must go through a **jump server**. You cannot connect to production databases directly from your laptop. This applies to both SQL MI and Snowflake. You also need to activate the relevant `Az-SG-ARP-Prd-*` or `Az-SG-Engage-Prd-*`  role using PIM [here](https://portal.azure.com/#view/Microsoft_Azure_PIMCommon/ActivationMenuBlade/~/aadgroup).

## Environments · Notes
_chunk 451 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/environments.md_

- **Local** is not listed above — your local environment runs via ARP Runner / Yarp at `localhost:5001` against the Astromart (ID=1) test tenant.
- **CICD** is the canary for `main` health. If CICD is broken, it means something merged that shouldn't have.
- **Staging is customer-accessible** — treat it with the same care as production. Do not use it for exploratory testing.
- **Production access** requires a logged incident or change request. Never apply ad hoc fixes directly to production.

[Tomorrowland - Environments (Confluence)](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475523743809/Tomorrowland+-+Environments)

---

*Back: [High Level Design](high-level-design.md) · Next: [Technology Stack](technology-stack.md)*

## Greenplum (legacy) · Overview
_chunk 452 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/greenplum.md_

Greenplum is the legacy analytics warehouse, based on PostgreSQL. It is being retired in favour of [Snowflake](snowflake.md). Expect to encounter both during the migration — some clients are fully on Snowflake, some are still served by Greenplum.

Same conceptual model as Snowflake: an ARDM schema per client holds the raw transaction data, and a per-client Secure schema sits alongside it for data that searches join against ARDM at query time.

---

## Greenplum (legacy) · Clusters, databases, and schemas
_chunk 453 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/greenplum.md_

Greenplum deployments are split across a production cluster and a non-production cluster:

| Environment | Cluster | Database | ARDM schema | Secure schema |
|---|---|---|---|---|
| Production | Prod cluster | `appriss` | `ardm_<abbreviation>` | `secure_{clientId}` |
| Staging | Non-prod cluster | `dev` | `ardm_<abbreviation>` | `secure_{clientId}` |
| Dev | Non-prod cluster | `swp_dev` | `ardm_<abbreviation>` | `secure_{clientId}` |
| QA | Non-prod cluster | `swp_qa` | `ardm_<abbreviation>` | `secure_{clientId}` |
| CICD | Non-prod cluster | `swp_cicd` | `ardm_<abbreviation>` | `secure_{clientId}` |

---

## Greenplum (legacy) · Per-client Secure schema
_chunk 454 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/greenplum.md_

Per-client Secure schemas (`secure_{clientId}`, e.g. `secure_001`) sit alongside the ARDM schemas in the same database, managed by the `Sources/Databases/Ardm.Secure/` EF project.

For what these schemas contain and why they exist alongside ARDM, see [Snowflake — Per-Client Secure Schema](snowflake.md#per-client-secure-schema). The Snowflake `C{id}_{abbr}` schema is the Greenplum `secure_{clientId}` schema's successor.

---

## Greenplum (legacy) · Current Greenplum clusters
_chunk 455 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/greenplum.md_

Greenplum is deployed across a mix of LA4 data-centre clusters (our on-prem footprint) and Azure clusters in both US West 2 and North Europe. Walmart run their own separate pair of clusters.

| Cluster | Full name | Location | Prod? | Version | Nodes | Size | IP | Direct (admin) | PgBouncer (service) | Supports |
|---|---|---|---|---|---|---|---|---|---|---|
| GP1 | USDEVGP1 | Azure (US West 2) | N | 6.28.2 | 8 | 62TB | 10.134.29.4 | TCP-6432 | TCP-5432 | Dev cluster |
| GP3 | USPRODGP3 | LA4 | Y | 6.28.2 | 8 | 240TB | 10.252.68.80 | TCP-5432 | TCP-6432 | ARDM (US), Secure (US) |
| GP4 | EUDEVGP4 | Azure (North Europe) | N | 6.24.3 | 2 | 6TB | 10.134.12.4 | TCP-6432 | TCP-5432 | Dev cluster |
| GP6 | USPRODGP6 | LA4 | Y | 6.28.2 | 8 | 240TB | 10.252.68.70 | TCP-5432 | TCP-6432 | ARDM (US), Identify (US), Secure (EU) |
| GP8 | EUPRODGP8 | Azure (North Europe) | Y | 6.28.2 | 8 | 125TB | 10.209.32.5 | TCP-6432 | TCP-5432 | ARDM (EU), Secure (EU) |
| GP9 | USPRODGP9 | LA4 | Y | 6.28.2 | 8 | 335TB | 10.252.168.120 | TCP-5432 | TCP-6432 | ARDM (EU), Secure (EU) |
| GP10 | USPRODGP10 | Azure (US West 2) | Y | 6.28.2 | 8 | 32TB | 10.201.32.8 | TCP-6432 | TCP-5432 | ARDM (US), Secure (US) |
| GP11 | USPRODGP11 | Azure (US West 2) | Y | 6.28.2 | 8 | — | 10.201.36.8 | TCP-6432 | TCP-5432 | ARDM (US), ARDM (Wal) |
| Prod_Walmart | — | Walmart | Y | 6.24.3 | 8 | 48TB | 10.34.17.229 | TCP-5432 | TCP-6432 | Secure (Wal), ARDM (Wal) |
| Dev_Walmart | — | Walmart | N | 6.24.3 | 8 | 12TB | 10.34.28.214 | TCP-5432 | TCP-6432 | Dev cluster |

**Direct vs PgBouncer ports:** the direct port is for admin use; application services connect via PgBouncer (connection pooling).

**Service DNS naming:** prod clusters resolve via `{cluster}.prod.retail` (e.g. `gp7.prod.retail`); non-prod via `{cluster}.test.retail` (e.g. `gp4.test.retail`).

For per-cluster GPCC links, Azure resource links, and sizing/performance guidance, see the source Confluence page: [Current Greenplum Clusters](https://trebuco.atlassian.net/wiki/spaces/ARIT/pages/474726957062/Current+Greenplum+Clusters).

---

## Greenplum (legacy) · Evolution of analytics data
_chunk 456 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/greenplum.md_

```
CRDM (per-client SQL Server)
    → ARDM in Greenplum (schema-per-tenant)
        → ARDM in Snowflake (schema-per-tenant, current target)
```

---

*Back: [Database Architecture](../databases.md)*

## HATR — High Availability Task Runner · Overview
_chunk 457 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

HATR is the Secure Platform's background job runner. Every scheduled piece of work — metric generation, work item generation, housekeeping, reference data loads, scheduled reports — runs on HATR. User-initiated long-running operations (async searches, Excel exports, PDF exports) run on HATR too.

It's built on **Azure Durable Functions**, which gives it the high-availability properties its name implies: orchestrations checkpoint their state, so if a worker dies mid-job, another worker resumes from the last checkpoint instead of starting over.

---

## HATR — High Availability Task Runner · Architecture
_chunk 458 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

HATR deploys as two separate Azure Function Apps, each with its own Durable Functions task hub:

| Function App | Hub name | Runs |
|---|---|---|
| SystemTasks | `%DeploymentSlot%SystemTasks` | Scheduled jobs (metrics, work items, housekeeping, reference data) |
| UserTasks | `%DeploymentSlot%UserTasks` | User-triggered work (async searches, exports) |

Split so that a flood of user exports can't block system-critical scheduled tasks.

**Key files:**
- `Sources/Hatr/ApprissRetail.Secure.Hatr/HatrTask.cs` — base task class
- `Sources/Hatr/ApprissRetail.Secure.Hatr/HatrScheduledTask.cs` — scheduled variant with locks and retries
- `Sources/Hatr/ApprissRetail.Secure.Hatr/HatrPosDataScheduledTask.cs` — base task for tasks which should wait for transaction data availability before running  
- `Sources/Core/Core/Hatr/HatrService.cs` — the public API that apps use to enqueue/cancel/check tasks

---

## HATR — High Availability Task Runner · User tasks vs system tasks
_chunk 459 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

The two function apps exist because the two task shapes have different triggers, lifetimes, and failure modes.

| | User tasks | System tasks |
|---|---|---|
| **Trigger** | A user action in the web app (clicking "Export to Excel", running a search) | A schedule — cron-like or interval |
| **Purpose** | Long-running work submitted fire-and-forget so the UI thread isn't blocked. Classic examples: async searches, Excel/PDF exports | Scheduled business work (metric generation, work item generation, report generation) and maintenance (housekeeping, reference-data loads) |
| **Lifetime** | Usually minutes; bounded by the user's patience | Seconds to hours; bounded by the data they're processing |
| **Status** | Polled by the UI via Redis-backed `HatrTaskStatus` so the page can show progress and results | Logged; surfaced in the Durable Functions Monitor |
| **Concurrency** | Many per user, many users at once | One per `(client, task)` at a time (distributed lock) |

Splitting them across function apps isolates the noisy neighbours — a user-export spike can't starve scheduled work that has SLAs.

---

## HATR — High Availability Task Runner · The task abstraction
_chunk 460 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

Every task implements `IHatrTask` or extends `HatrTask<TTaskInput>`. Inputs are strongly typed and validated via `IHatrTaskInput.IsInputValid()` before the task runs.

```csharp
public sealed class MyTask : HatrTask<MyTaskInput>
{
    public override async Task<HatrTaskResult> ExecuteAsync(
        HatrOrchestrateContext context, MyTaskInput input) { ... }
}
```

Scheduled tasks extend `HatrScheduledTask<TTaskInput>` and override `GetSchedule()` to declare when they run. Scheduled POS-data tasks extend `HatrPosDataScheduledTask` to add a Go/No-Go check that waits for upstream data loads.

Tasks are **discovered by reflection** at startup — `HatrTaskMetadataHelper` scans the entry assembly for `IHatrTask` implementations and registers them. No central registry to edit when adding a task.

The enum in `Sources/Hatr/ApprissRetail.Secure.Hatr.Common/HatrTaskNames.cs` holds stable task IDs (1–48 today) used for instance naming and correlation.

---

## HATR — High Availability Task Runner · High availability
_chunk 461 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

Three mechanisms combine to make HATR resilient:

### Durable checkpointing
Durable Functions persists orchestration state after every `await`. A worker crash doesn't lose state — another worker picks up from the last checkpoint and replays forward.

### Distributed locking
Scheduled tasks acquire a Durable Entities lock keyed by `TaskClientLock → {ClientID:000}x{TaskName}` before executing (`HatrScheduledTask.GetLockKvps()`). This guarantees only one instance of a given task runs per client at a time, even if the scheduler fires twice or two workers pick up the same trigger.

### Retry with exponential backoff
`HatrOrchestrateContext` wraps activities in a retry policy — 3 retries, 10-second base delay, 2× backoff (configured per task in `HatrOrchestrateContext.cs`). Transient failures (a brief Snowflake outage, a throttled DB call) self-heal.

---

## HATR — High Availability Task Runner · Scheduling
_chunk 462 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

Schedules are declared in code, not in a database. A task's `GetSchedule()` returns a `HatrSchedule` with one of two modes:

| Mode | Behaviour |
|---|---|
| `Schedule` | Runs once per day at a specific time (e.g. daily housekeeping at 03:00) |
| `Interval` | Runs every N minutes (e.g. work item generation every 15 min) |

`HatrSchedule.GetNextTriggerTimeUtc()` computes the next fire time. POS-data tasks delay their own next run by 15 minutes (or one interval) if the Go/No-Go check says upstream data isn't ready yet — they don't fail, they just wait.

---

## HATR — High Availability Task Runner · Multi-tenancy
_chunk 463 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

One HATR deployment serves every tenant. Tenant context rides on the request: `HatrTaskRequest.ClientID` and `UserID` flow through to every activity. Instance IDs encode the tenant — `{ClientID:000}x{TaskID}` — which makes it easy to filter the Monitor dashboard to a single client.

The distributed lock is keyed by `(ClientID, TaskName)`, so client A's metric generation doesn't block client B's.

---

## HATR — High Availability Task Runner · Observability
_chunk 464 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

Tasks log through `ILogger` on the orchestration context. Structured fields flow into New Relic / Grafana Cloud via the OTEL pipeline (see `observability.md`).

| Concern | Mechanism |
|---|---|
| Execution logs | `context.Log.LogInformation(...)`, `LogError(...)` |
| Live status (user-visible) | `context.UpdateCustomStatus(...)` — shown in the Durable Functions Monitor |
| Client-side status polling | `HatrTaskStatus` (Running / Complete / Failed) pushed to Redis |
| Traces | Durable Functions v2 distributed tracing enabled in `host.json` |

The **Monitor** project (`ApprissRetail.Secure.Hatr.Monitor`) hosts the Durable Functions dashboard, running read-only in production.

---

## HATR — High Availability Task Runner · Adding a new task
_chunk 465 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

1. Define an input type implementing `IHatrTaskInput` with an `IsInputValid()` method.
2. Add a new entry to `HatrTaskNames.cs` (claim the next ID).
3. Subclass `HatrTask<TInput>` (one-shot) or `HatrScheduledTask<TInput>` (scheduled). Implement `ExecuteAsync`; override `GetSchedule()` for scheduled variants.
4. Place the file under the appropriate project — `ApprissRetail.Secure.Hatr.SystemTasks` for scheduled system jobs, `ApprissRetail.Secure.Hatr.UserTasks` for user-triggered work.
5. Reflection picks it up on the next cold start — nothing else to register.

Invoke it from application code via `IHatrService` (`Sources/Core/Core/Hatr/HatrService.cs`).

---

## HATR — High Availability Task Runner · Related
_chunk 466 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/hatr.md_

- See `features/work-item-generation.md`, `features/metric-generation.md`, `features/reports.md`, `features/location-hierarchy.md` for specific HATR-driven pipelines.
- For the full catalogue of current tasks, look at implementations of `HatrTask` / `HatrScheduledTask` — reflection-driven registration makes the class list the source of truth.
- The Cache service (`cache.md`) publishes `HatrTaskStatus` updates to Redis for client polling.

## Location Hierarchy · Overview
_chunk 467 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

A **hierarchy** in Secure is the tree structure that organises a tenant's physical locations — typically stores grouped by country → region → district → store, up to six levels deep. It's the primary data-access boundary: a user's hierarchy membership determines which stores they can see in searches, reports, dashboards, and work items.

This doc covers how hierarchies are generated, stored, and consumed, and the in-flight migration to **Square Hierarchy** — a new implementation that removes the strict-tree job, unifies the schema with Incident/Engage, and supports non-strict hierarchies (a child with multiple parents).

For the design document, see [Secure Platform Cohesion — Square Hierarchy](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475608973313/Secure+Platform+Cohesion+-+Square+Hierarchy).

> **Schema at a glance.** Legacy hierarchy tables and stored procedures live in the `structure` schema of the Platform DB. Square Hierarchy's tables and stored procedures live in the `secure` schema and — for anything Square-specific — are prefixed with `SquareHierarchy` (e.g. `secure.SquareHierarchyMigrateLocationHierarchies`).

---

## Location Hierarchy · Why two implementations exist
_chunk 468 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

The classic hierarchy flow is strict: the Secure job rebuilds a fully-normalised tree from reference data, and any integrity violation (e.g. a store appearing under two parents) aborts the load. Square Hierarchy trusts customer-sent data instead — multiple parents are honoured, integrity checking moves to a separate monitoring job — and keeps schema/behaviour compatible with MSSQL, ARDM, and Snowflake so one table set serves all three.

Both run side-by-side today. Feature flags gate which implementation writes and reads.

---

## Location Hierarchy · Classic (legacy) flow
_chunk 469 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

```
DataOps loads reference_location (ARDM)        [No change in Square]
    ↓
YADL copies data → place.Location (MSSQL)      [No change in Square]
    ↓
BuildLocationHierarchyFromReference (HATR)     [Dropped in Square]
    ↓ builds strict tree, aborts on invalid data
structure.LocationHierarchyMaster (MSSQL)
structure.LocationHierarchyMember
structure.LocationHierarchyMemberLocations
    ↓
Search joins to secure structure tables (ARDM + MSSQL) to filter by user-visible stores
```

The integrity-abort behaviour is the pain point: a single bad row from a customer holds up the entire hierarchy rebuild, which requires manual DataOps intervention before searches can see the new data.

**Key files:**
- `Sources/Core/Core/Hierarchy/HierarchyService.cs` — abstract base service
- `Sources/Core/Core/Hierarchy/Location/LocationHierarchyService.cs` — location implementation
- `Sources/Core/Core/Hierarchy/Job/Tasks/BuildLocationHierarchyFromReference.cs` — strict-tree build job
- `Sources/Core/Core/Hierarchy/Job/Tasks/ReplicateHierarchiesToDbTask.cs` — replicates between MSSQL and ARDM

---

## Location Hierarchy · Square Hierarchy
_chunk 470 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

The design explicitly trusts customer-sent data. Multiple parents are allowed. Integrity checking becomes a separate, notifying concern rather than a blocking one.

### What changes

1. **Drop** the strict-tree build job (classic's `BuildLocationHierarchyFromReference`).
2. **Introduce** a single table in each engine that joins stores to hierarchy members without the intermediate master/member normalisation:
   - `[secure].[HierarchyLocations]` (Platform DB, MSSQL)
   - `secure_hierarchylocations` (ARDM / Snowflake)
3. **Move** maintenance of those tables to the UI and the SSO sign-in flow — no data loads, no YADL, no rebuild job.
4. **Keep** hierarchy 1 (the canonical customer hierarchy) locked — levels and members are not user-editable. Custom hierarchies (IDs > 1) are fully user-managed.

### What stays the same

- DataOps loads `reference_location` (ARDM).
- YADL copies reference data to `place.Location` (MSSQL) for non-hierarchy uses (store names, geo, etc.).
- SSO sign-in still maps IDP claims to hierarchy membership.

### Query-time routing

Searches with hierarchy restrictions pick the join target based on the hierarchy ID:

| Hierarchy ID | ARDM join | MSSQL join |
|---|---|---|
| 1 (canonical) | `reference_location` | `place.Location` |
| &gt; 1 (custom) | `secure_hierarchyLocations` | `place.HierarchyLocations` |

The user's visible stores come from joining the chosen table against `secure_locationUsers` and `secure_memberUsers`, then left-joining (null-check) to the `Header` table.

---

## Location Hierarchy · Feature flags
_chunk 471 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

Read/write for Square Hierarchy is gated per concern so the two implementations can run side-by-side and cut over incrementally:

| Flag | Effect |
|---|---|
| `Feature.SquareHierarchies.HierarchyService.WriteToSquareHierarchy` | Writes (UI edits, SSO sign-in) go to the new tables |
| `Feature.SquareHierarchies.HierarchyService.ReadFromSquareHierarchy` | Reads come from the new tables |
| `Feature.SquareHierarchies.HierarchyService.ThrowOnSquareHierarchyFailure` | Surface Square failures instead of silently falling back to legacy |
| `Feature.SquareHierarchies.UseSquareHierarchyInSqlGenerator` | The SQL generator emits joins against the Square tables instead of the legacy structure tables |
| `Feature.Hierarchies.EnableLegacyHierarchy` | Keep classic path active (dual-write during migration) |

Flag evaluation lives in `Sources/Core/Core/Hierarchy/Location/LocationHierarchyService.cs`.

> **Cache note.** After flipping any of these flags, always clear the client's platform cache (`../cache.md`) — hierarchy lookups are cached aggressively.

---

## Location Hierarchy · Migration
_chunk 472 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

A one-time migration HATR task moves existing structure data into the Square tables.

| Task | File |
|---|---|
| `MigrateToSquareHierarchyTask` | `Sources/Hatr/ApprissRetail.Secure.Hatr.SystemTasks/MigrateToSquareHierarchy/MigrateToSquareHierarchyTask.cs` |
| Activity | `…/MigrateToSquareHierarchyActivity.cs` |
| Task ID | `HatrTaskNames.MigrateToSquareHierarchyTask = 32` |

The task uses the durable-orchestrator pattern (see `../hatr.md`). It's triggered from the System Tasks UI per client with the required feature flags already turned on.

Canonical runbook per client:

1. Set `Feature.SquareHierarchies.HierarchyService.WriteToSquareHierarchy = true`.
2. Clear the cache.
3. Run `MigrateToSquareHierarchyTask` from the System Tasks UI, selecting the target client.

Once writes are going to Square and migration is complete, finish the cutover:

4. Flip `Feature.SquareHierarchies.HierarchyService.ReadFromSquareHierarchy = true` — reads now come from the Square tables.
5. Flip `Feature.SquareHierarchies.UseSquareHierarchyInSqlGenerator = true` — SQL generation joins against the Square tables instead of the legacy structure tables.
6. Turn off `Feature.Hierarchies.EnableLegacyHierarchy` — stops dual-write to the legacy `structure` tables.
7. Clear the cache again.

---

## Location Hierarchy · Stored procedures
_chunk 473 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

### Used by the migration task

Two sprocs handle the one-shot move of existing data into the Square tables:

- `secure.SquareHierarchyMigrateLocationHierarchies`
- `secure.SquareHierarchyMigrateLocationUserAssignments`

### Used at runtime by the app

These are called in normal operation — import/edit/lookup paths — not by the migration task:

- `secure.SquareHierarchyImportMembersFromReference` — pull new members in from reference data
- `secure.SquareHierarchyLocationUserAssignmentInsert` — write user-to-member assignments from the UI and SSO
- `sso.SquareHierarchyGetLocationHierarchyMembersWithMember` and peers — SSO-time lookups for mapping IDP claims to hierarchy members

---

## Location Hierarchy · Storage
_chunk 474 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

### Platform DB (SQL MI)

| Table | Purpose |
|---|---|
| `place.Location` | Source of the canonical hierarchy (hierarchyID = 1) — stores + their level codes. YADL-maintained |
| `secure.HierarchyLocations` | Square: stores ↔ hierarchy-member mappings for **custom** hierarchies (hierarchyID > 1). Denormalised 6-level codes |
| `secure.LocationHierarchyUserAssignments` | Square: user ↔ hierarchy-member memberships |
| `structure.LocationHierarchyMaster` | Hierarchy metadata — still used by Square Hierarchy to drive level flips and rename operations |
| `structure.LocationHierarchyMember` | Legacy: members per hierarchy level |
| `structure.LocationHierarchyMemberLocations` | Legacy: store ↔ member mapping |

### ARDM (Snowflake / Greenplum)

| Table | Purpose |
|---|---|
| `secure_hierarchylocations` | Replicated Square table — read target for custom hierarchies |
| `secure_locationhierarchyuserassignments` | Replicated Square table |
| `reference_location` | Canonical location reference — read target for hierarchy 1 |

---

## Location Hierarchy · HATR integration
_chunk 475 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

| Task | Task ID | Role |
|---|---|---|
| `BuildLocationHierarchy` | 16 | Classic strict-tree build — dropped once on Square |
| `MigrateToSquareHierarchyTask` | 32 | One-time per-client data migration |
| `ReferenceDataCache`, `ReferenceDataBackLoad` | — | Load ARDM reference data into the Platform DB. "Reference" here means the full set of reference-data loads (stores, employees, etc. — not `reference_location` specifically). Unchanged between classic and Square |

See `../hatr.md`.

---

## Location Hierarchy · Consumers
_chunk 476 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

- **Searches** — hierarchy filtering joins happen inside `SearchAccess` during SQL generation. See `search.md`.
- **SSO sign-in** — IDP claims (level, value) map to hierarchy members; user gets `locationUsers`/`memberUsers` rows for the stores they can see.
- **Dashboards and Reports** — hierarchy filters flow through `LocationHierarchyDashboardParameter` and report-level hierarchy restrictions.
- **Permissions** — `HierarchyPermissions` gates create/edit/read of hierarchies themselves.
- **Profiles** — user/cashier profiles are scoped by hierarchy membership.

---

## Location Hierarchy · Key file pointers
_chunk 477 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

| Concern                                        | File                                                                            |
|------------------------------------------------|---------------------------------------------------------------------------------|
| Base hierarchy service                         | `Sources/Core/Core/Hierarchy/HierarchyService.cs`                               |
| Location hierarchy + flag logic                | `Sources/Core/Core/Hierarchy/Location/LocationHierarchyService.cs`              |
| Migration orchestrator                         | `Sources/Hatr/.../MigrateToSquareHierarchy/MigrateToSquareHierarchyTask.cs`     |
| Migration activity                             | `Sources/Hatr/.../MigrateToSquareHierarchy/MigrateToSquareHierarchyActivity.cs` |
| SSO Service                                    | `Sources/UI/SignIn.Common/Services/SsoService.cs`                               |
| Platform.\*Hierarchy\* SQl generator functions | `Sources/Core/Core/Data/FunctionFramework/Functions/Hierarchy/Location/*.cs`    |

## Location Hierarchy · Related
_chunk 478 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/location-hierarchy.md_

- Design: [Secure Platform Cohesion — Square Hierarchy](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475608973313/Secure+Platform+Cohesion+-+Square+Hierarchy)
- `search.md` — hierarchy filtering during search execution
- `reference-data.md` — how `reference_location` and `place.Location` get loaded
- `../hatr.md` — migration task orchestration
- `../cache.md` — required cache clear after flag changes

## Lunar (Database Installer) · Overview
_chunk 479 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/lunar.md_

Lunar is a .NET 8 console app that orchestrates database provisioning: creating databases, running EF Core migrations, and loading seed data. It lives in `Sources/Databases/Installer/`.

It supports every database in the platform — SQL MI (configuration + per-tenant platform/reference), Snowflake, and Greenplum — via a provider pattern.

---

## Lunar (Database Installer) · Key components
_chunk 480 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/lunar.md_

| File | Role |
|---|---|
| `Program.cs` | Entry point — DI setup, logging, provider registration |
| `Application.cs` | Main orchestrator — coordinates migrations and seeding across clients in parallel |
| `Database/Providers/` | Database provider implementations (see below) |
| `DatabaseInstaller/` | Migration and seeding services |
| `BulkCopyInfoProviders/` | Table-specific bulk insert/upsert mappers (9 providers) |
| `SeedDefinition/` | Seed file loading and execution |

---

## Lunar (Database Installer) · Database providers
_chunk 481 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/lunar.md_

Lunar uses a provider pattern (`IDatabaseProvider`) to support multiple database technologies:

| Provider | Target |
|---|---|
| `MsSqlDatabaseProvider` | SQL Server — transactions, bulk copy |
| `SnowflakeDatabaseProvider<T>` | Snowflake ARDM — EF Core with Snowflake NuGet, per-client schema |
| `PostgresqlDatabaseProvider<T>` | PostgreSQL/Greenplum ARDM — Npgsql, schema creation, retries |
| `EntityFrameworkDatabaseProvider<T>` | Generic EF Core wrapper for schema-based databases |
| `EmptyDatabaseProvider` | No-op for skipping database operations |

---

## Lunar (Database Installer) · Seed data layering
_chunk 482 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/lunar.md_

Seed data originates in `arpfiles/repo` (a separate repo at `C:\arpfiles`). Seeds are applied in layers, with later layers overwriting earlier ones for the same key:

| Layer | Source | Purpose |
|---|---|---|
| 1. Platform | `repo/platform/seed/*.json` | Base defaults shared across all clients |
| 2. Platform environment | `repo/platform/seed/*.{environment}.json` | Environment-specific platform overrides |
| 3. Client file | `repo/{clientId}/seed/*.json` | Per-client customisations |
| 4. Client manifest | `seed-manifest.json` | Embedded client definitions |
| 5. Client environment manifest | `seed-manifest.{environment}.json` | Environment-specific client overrides |

Each layer merges on unique key — same key in a later layer overwrites the earlier value. This allows platform defaults to be overridden per-client, and further overridden per-environment.

Lunar tracks which seeds have been applied in the `__SeedHistory` table to avoid re-seeding records which already exist or has been modified in-app. 

`BulkCopyInfoProviders` (in `Installer/BulkCopyInfoProviders/`) map seed data to target database table columns for bulk insert.

---

## Lunar (Database Installer) · EF Core Migrations
_chunk 483 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/lunar.md_

All schema changes are tracked via EF Core migrations. Each database project has a `Migrations/` folder. **All schema changes — tables, columns, sequences, constraints — must go through EF Core migrations.** Do not create standalone SQL files for schema changes; the `Programmability/` folder is only for stored procedures and functions. 

Each migration has:
- **Up()** — applies the change
- **Down()** — reverts it (for dev rollback; not used in production)
- **Designer file** (`.Designer.cs`) — model snapshot

SQL Server migrations use PascalCase; PostgreSQL migrations use snake_case.

### Creating a new migration

1. Make any necessary changes to the entity model or DbContext configuration in the relevant database project.
2. From `Sources/Databases/Platform` or `Sources/Databases/Snowflake` run:

```bash
dotnet ef migrations add <MigrationName>
```

For example, for Snowflake:

```bash
cd Sources/Databases/Snowflake
dotnet ef migrations add AddSomeTable
```

3. EF generates a migration file with `Up()` and `Down()` methods. If EF detects model drift from previous migrations, it will include those changes automatically.
4. For custom SQL that EF cannot express natively (e.g. creating sequences, running procedural blocks), use `migrationBuilder.Sql("...")` inside the `Up()` method. We try to avoid this where possible, but sometimes it is necessary.
5. To preview the sql EF will run when applying your migration(s), use `dotnet ef migrations script -i {StartingMigrationName} {TargetMigrationName}`
6. To remove the last migration: `dotnet ef migrations remove`

---

## Lunar (Database Installer) · Programmability
_chunk 484 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/lunar.md_

Stored procedures and functions live under `Programmability/` in each database project, organized by schema (e.g. `dbo`, `incident`, `secure`, `metric`).

`Common/ServerWideScripts/` contains server-level SQL scripts run during provisioning:
- `Script.CreateLoginsAndUsers.sql` — logins, users, permissions (Azure-aware)
- `Script.ServerConfiguration.sql` — server settings
- `Script.MaintenanceSolution.sql` — comprehensive index/stats maintenance toolkit
- `Script.DbShrink.sql`, `Script.ColumnStoreAdvMaint.sql`, etc.


---

*Back: [Database Architecture](../databases.md)*

## Metric Generation · Overview
_chunk 485 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

Metrics are period-aggregated KPIs (e.g. "total refunds this week for store 42") calculated from search results and stored in the Metric database. They power store/cashier profiles, dashboards, AI Outliers, and trending features.

This document covers the HATR metric generation task and activity. For how metrics feed into AI Outliers, see `ai-outliers.md`.

---

## Metric Generation · Where Metrics Are Used
_chunk 486 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

| Consumer | How it uses metrics |
|---|---|
| **Store/Cashier profile charts** | Displays metric values over time on profile pages (e.g. refunds per week for a store). Metrics tagged for profiles appear as trend charts. |
| **AI Outliers** | IsolationForest model trains on metrics tagged `secureai-store` or `secureai-cashier` to identify anomalous entities. See `ai-outliers.md`. |
| **Metric search composer** | Users can build searches that query metric values directly, joining metric data to other data areas. |
| **SRA dashboard** | Store Risk Assessment dashboard uses dedicated SRA-category metrics to score and rank stores by risk indicators. |

---

## Metric Generation · Overview
_chunk 487 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

```
Metric Definitions (METRIC_METRICDEFINITION)
  Define: which search to run, which field to aggregate, which keys to group by, which periods
    ↓
MetricGeneratorTask (HATR, daily 6:00 AM)
  For each calendar + period type combination:
    ↓
  MetricGeneratorActivity
    ↓
  MetricCalculatorJob
    Execute search → aggregate results → INSERT/UPDATE metric values
    ↓
Metric Tables (METRIC_METRICS_{PERIODTYPE}_{KEYCOUNT}KEY)
```

---

## Metric Generation · HATR Task
_chunk 488 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

**File:** `Sources/Hatr/ApprissRetail.Secure.Hatr.SystemTasks/MetricGenerator/MetricGeneratorTask.cs`

| Property | Value |
|---|---|
| Task ID | `298f62d8-2165-40fc-af36-acfa736bf4d7` |
| Schedule | Daily at 6:00 AM |
| Task name enum | `HatrTaskNames.MetricGenerator` (21) |
| Base class | `HatrPosDataScheduledTask<MetricGeneratorInput>` |

The task inherits from `HatrPosDataScheduledTask`, which means it waits for POS data availability before executing (via `HatrPosDataGoNoGoCheckActivity`). If data is unavailable, it retries after 15 minutes.

### Default Scheduled Input

```json
{
  "CalendarFilter": ["/system/calendar/business.cal"],
  "PeriodFilter": ["Day"],
  "SourceAppFilter": ["store"],
  "RecalculateIfExists": true,
  "RecalculateLowerPeriodGrainIfExists": false,
  "DeleteIfNoSourceData": false
}
```

### Orchestration

`MetricGeneratorTask.OrchestrateAsync()`:

1. Recalculates metrics **3 days backward** for scheduled runs to account for trickle-loaded data
2. Retrieves calendar periods from input via `GetCalendarPeriods()`
3. Groups periods by type (Day, Week, Month, Quarter, Year)
4. Creates a `MetricGeneratorActivityInput` for each period
5. Calls activities concurrently — max 3 concurrent for Day periods, 1 for others
6. Logs failures and throws if any activities fail

---

## Metric Generation · HATR Activity
_chunk 489 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

**File:** `Sources/Hatr/ApprissRetail.Secure.Hatr.SystemTasks/MetricGenerator/MetricGeneratorActivity.cs`

The activity:
1. Creates a job context adapter from the input parameters
2. Builds arguments for the metric calculator (From/To dates, Period Type, Calendar, filters)
3. Instantiates `MetricCalculatorJob`
4. Executes the job

### Input

**MetricGeneratorActivityInput** (`Sources/Hatr/.../MetricGenerator/Inputs/MetricGeneratorActivityInput.cs`):

| Field | Purpose |
|---|---|
| From, To | Date range for the period |
| Calendar | Calendar VFP (e.g. `/system/calendar/business.cal`) |
| PeriodType | Day / Week / Month / Quarter / Year |
| MetricIdFilter[] | Specific metric IDs to calculate (optional) |
| SourceAppFilter[] | Filter by source app, e.g. `["store"]` |
| TagFilter[] | Filter by metric tags (optional) |
| CategoryFilter[] | Filter by metric categories (optional) |
| RecalculateIfExists | Force recalculation of existing values |
| RecalculateLowerPeriodGrainIfExists | Recalculate lower grain aggregations |
| DeleteIfNoSourceData | Delete metric values when source data returns 0 rows |

---

## Metric Generation · MetricCalculatorJob
_chunk 490 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

**File:** `Sources/Core/Core/Metrics/MetricCalculator/MetricCalculatorJob.cs`

The core calculation engine. Execution flow:

1. Parse input parameters into `MetricCalculatorInput`
2. Retrieve targeted metric definitions (filtered by calendar, period type, IDs, source app, tags, category, enabled/not-deleted)
3. Group metrics by SSR VFP and key count — multiple metric definitions can share the same powering search, so grouping by VFP means the search only needs to execute once and the results are reused to calculate all metrics in the group
4. For each group, get the appropriate metric calculator action for the database type
5. Execute the action for each period — runs the search once, then aggregates the results into each metric in the group
6. Clear the metric query metadata cache
7. Update monitoring stats
8. Optionally poke SecureAI if `Feature.Metric.PokeSecureAiWhenComplete` is enabled

### Calculation Actions

Different database backends have their own action implementations:

| Database | Action | Purpose |
|---|---|---|
| MSSQL | `MsSqlMetricCalculateFromSearchAction` | Execute search, aggregate, write to SQL Server |
| MSSQL | `MsSqlMetricCalculateFromLowerPeriodGrainAction` | Aggregate from Day → Week → Month etc. |
| MSSQL | `MsSqlMetricCalculateFromExternalSourceAction` | Calculate from external data source |
| Snowflake | `SnowflakeMetricCalculateFromSearchAction` | Same pattern for Snowflake |
| Snowflake | `SnowflakeMetricCalculateFromLowerPeriodGrainAction` | Lower grain aggregation for Snowflake |
| PostgreSQL | `PostgresqlMetricCalculateFromSearchAction` | Same pattern for Greenplum/Postgres |
| PostgreSQL | `PostgresqlMetricCalculateFromLowerPeriodGrainAction` | Lower grain aggregation for Postgres |

### SQL Operations per Metric Group

Each calculation action generates:
1. **SELECT INTO temp table** — execute the base search
2. **UPDATE** — update existing metric values that match
3. **INSERT** — insert new metric values
4. **DELETE** — remove metrics with no source data (if configured)
5. **DROP** — clean up temp tables

### Lower Period Grain Aggregation

When `AggregateFromLowerPeriodGrains` is enabled (default: true), higher-period metrics are calculated by aggregating lower-period values rather than re-running the full search:

```
Day → Week → Month → Quarter → Year
```

This is an optimisation — it avoids running expensive searches for every period type. However, unique-count fields cannot be re-aggregated from lower grains and will fall back to `CalculateFromSearchAction`.

---

## Metric Generation · Metric Definitions
_chunk 491 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

Metric definitions live in the Metric database in the `METRIC_METRICDEFINITION` table.

### Key Fields

| Field | Purpose |
|---|---|
| ID | Unique identifier |
| MetricName | Internal name |
| DisplayName | User-facing name |
| VirtualFilePath | SSR (search) that provides the source data |
| Key1KeysetID, Key1SourceField | First aggregation key (e.g. store) |
| Key2KeysetID, Key2SourceField | Second aggregation key (e.g. cashier) |
| Key3KeysetID, Key3SourceField | Third aggregation key |
| MetricValueSourceField | Which SSR field to aggregate |
| FunctionName | Aggregation function: Sum, Average, Percent |
| MetaNumerator, MetaDenominator | For percent calculations |
| PeriodType | Flag enum of supported periods (Day\|Week\|Month etc.) |
| CalendarVirtualFilePath | Which calendar drives the metric |
| SourceApp | Source application (e.g. `"store"`) |
| Category | Grouping category |
| Tags | Space-separated tags (e.g. `"secureai-store"`) |
| UsageType | System (1) or User (2) |
| Disabled | Prevents calculation |
| Deleted | Soft delete |

### Period Types

`Sources/Schema/ApprissRetail.Secure.Common/Calendar/PeriodType.cs`

| Value | Name |
|---|---|
| 32 | Day |
| 64 | Week |
| 128 | Month |
| 256 | Quarter |
| 512 | Year |

These are flags — a metric definition can support multiple period types (e.g. `Day | Week | Month`).

### OOTB Category Metrics

The platform ships with out-of-the-box metrics under `/public/metric searches/ootb general/`. Each category has a cashier-level and store-level search:

| Category | Cashier VFP | Store VFP |
|---|---|---|
| Base transaction count | `.../base transaction count cashier totals.search` | `.../base transaction count store totals.search` |
| Exchange transactions | `.../exchange transactions.search` | `.../exchange transactions store totals.search` |
| Item discounts | `.../item discounts.search` | `.../item discounts store totals.search` |
| Line voids | `.../line voids.search` | `.../line voids store totals.search` |
| Line voids to zero | `.../line voids to zero.search` | `.../line voids to zero store totals.search` |
| No sale transactions | `.../no sale transactions.search` | `.../no sale transactions store totals.search` |
| Price overrides | `.../price overrides.search` | `.../price overrides store totals.search` |
| Refunds | `.../refunds.search` | `.../refunds store totals.search` |
| Voided transactions | `.../voided transactions.search` | `.../voided transactions store totals.search` |

All paths above are relative to `/public/metric searches/ootb general/`.

### SRA Dashboard Metrics

The Store Risk Assessment dashboard has its own metric searches:

| VFP | Metrics |
|---|---|
| `/system/ebr/metrics/search/SraMetricsByStore.search` | SRA store-level metrics: sales, refunds, line voids, post-tender voids, transaction cancels, manual price modifications, coupons, item coupons, tax modifications, suspended, no sales, transaction count (count + amount for each) |
| `/system/ebr/metrics/search/sratransactionmetricsbystore.search` | SRA transaction metrics: SRAValue, SRAPercToSales, SRACustomer, SRACustomerFreq, VPC, VPI, IPC, NonSRA totals |
| `/system/ebr/metrics/search/customertransactionsbystoreemployee.search` | CustomerCountByEmployee |

Metric definitions are seeded from `arpfiles/repo/platform/seed/metric_Definition.json`.

---

## Metric Generation · Metric Storage
_chunk 492 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

Metric values are stored in period-and-key-count-specific tables in the Metric database:

```
METRIC_METRICS_{PERIODTYPE}_{KEYCOUNT}KEY
```

For example: `METRIC_METRICS_WEEK_2KEY` for weekly metrics grouped by store + cashier.

### Table Columns

| Column | Purpose |
|---|---|
| PeriodValueID | Foreign key to the calendar period |
| MetricDefinitionID | Foreign key to the metric definition |
| Key1, Key2, Key3 | Aggregation key values (store number, cashier number, etc.) |
| Value | Calculated metric value |
| Numerator | For percent calculations |
| Denominator | For percent calculations |

### Stored Procedures

| Procedure | Purpose |
|---|---|
| `METRIC_METRICDEFINITIONSELECT` | Retrieve metric definitions |
| `METRIC_METRICDEFINITIONINSERT` | Create new definitions |
| `METRIC_METRICDEFINITIONUPDATE` | Update definitions (tags, enabled, etc.) |
| `METRIC_METRICPERIODKEYSETVALUEBLOCKDELETE` | Bulk delete metric values |
| `METRIC_PERIODVALUESELECT` | Retrieve period values for a calendar |
| `METRIC_METRICKEYDEFINITIONSELECTBYSOURCEAPP` | Retrieve key definitions |

---

## Metric Generation · Configuration
_chunk 493 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

| Config Item | Default | Purpose |
|---|---|---|
| `Metric.AggregateFromLowerPeriodGrains` | true | Enable lower grain optimisation |
| `Feature.Metric.PokeSecureAiWhenComplete` | false | Trigger SecureAI analysis after metrics complete |
| `Feature.MetricManager.SecureAIEnabled` | — | Enable SecureAI integration in Metric Manager |
| `Feature.MetricManager.ProfileMetrics_MaxNumber` | 10 | Max profile metrics |

### MetricCalculatorInput Defaults

| Parameter | Default | Purpose |
|---|---|---|
| SkipMetricCalculationWhen0BasedUponRows | true | Skip if no source data |
| AggregateFromLowerPeriodGrains | true | Optimise via aggregation |
| RecalculateIfExists | false | Force recalculation |
| OptimizeQuery | true | SQL query optimisation |
| SaveState | false | Persist job state for resumption |

---

## Metric Generation · Monitoring
_chunk 494 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/metric-generation.md_

`MetricStatusService` (`Sources/Core/Core/Metrics/Services/MetricStatusService.cs`) tracks generation health.

Stats updated per run:
- `{CalendarName}-{PeriodType}-Calculated` — count of metrics affected
- `{CalendarName}-{PeriodType}-Error` — error flag (0 or 1)
- `{CalendarName}-{PeriodType}-LastRan` — last execution timestamp

## Logging, Tracing, Metrics, and Observability · Overview
_chunk 495 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

This document covers how to log, trace, and emit metrics in the Secure platform and where that telemetry ends up.

For the full Confluence reference, see [Logs and Observability](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475135344725/Logs+and+Observability).

---

## Logging, Tracing, Metrics, and Observability · How to Log in .NET
_chunk 496 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

Use `Log.cs` (`Sysrepublic.Foundation.Logging.Log`). It wraps an `ILogger` and provides static convenience methods.

### Import

```csharp
using Sysrepublic.Foundation.Logging;
```

### Methods

All methods follow the signature pattern: `(string component, string sender, string message, IDirector director)`.

| Method | When to use |
|---|---|
| `Log.Audit(...)` | User-facing actions worth recording (logins, data changes) |
| `Log.Warning(...)` | Unexpected but recoverable situations |
| `Log.Exception(...)` | Unrecoverable errors — accepts an `Exception` object |

### Usage

Use `nameof` for the `component` and `sender` parameters:

```csharp
// Warning
Log.Warning(nameof(MetricService), nameof(this.GetAllMetricDefinitions),
    $"Duplicate metric definition ID {id} found for client '{this.director.ClientID}'.",
    this.director);

// Exception
Log.Exception(nameof(MetricService), nameof(this.GetAllMetricDefinitions),
    ex, this.director);

// Audit
Log.Audit(nameof(MetricService), nameof(this.SaveMetric),
    $"Metric {metricId} saved.", this.director);
```

Overloads without `IDirector` exist for cases where no director is available (e.g. startup code).

### Python

Use the standard `logging` module. The OTEL collector picks up Python logs the same way.

---

## Logging, Tracing, Metrics, and Observability · Distributed Tracing
_chunk 497 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

Distributed tracing is configured via OpenTelemetry auto-instrumentation. Traces are exported to the OTEL Collector alongside logs.

### Instrumented Applications

| Application | `service.name` | `service.namespace` | Instrumentation |
|---|---|---|---|
| PlatformUI | `platformui` | `frontend` | ASP.NET Core, HttpClient, SqlClient, Redis |
| SignIn | `signin` | `frontend` | ASP.NET Core, HttpClient, SqlClient |
| Yarp | `yarp` | `frontend` | ASP.NET Core, HttpClient, SqlClient |
| ControlPanel | `controlpanel` | `frontend` | ASP.NET Core, HttpClient, SqlClient, Redis (when `EnableRedis=True`) |
| SystemTasks | `systemtasks` | `backend` | Functions Worker, HttpClient, SqlClient, Redis |
| UserTasks | `usertasks` | `backend` | Functions Worker, HttpClient, SqlClient, Redis |
| DotNetApi | `dotnetapi` | `backend` | Functions Worker, HttpClient, SqlClient, Redis |

### How Tracing and Metrics are Configured

Three shared builders in `Sources/Schema/ApprissRetail.Common.Logging/` handle all signal configuration:

| Class | Signal | File |
|---|---|---|
| `CommonLoggerBuilder` | Logs | `CommonLoggerBuilder.cs` |
| `CommonTracingBuilder` | Traces | `OpenTelemetry/CommonTracingBuilder.cs` |
| `CommonMetricsBuilder` | Metrics | `OpenTelemetry/CommonMetricsBuilder.cs` |

All three share a single `BuildResourceBuilder()` method that sets resource attributes and resolves the deployment environment.

Each application wires up tracing and metrics in its `Program.cs`:

```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(tracerProviderBuilder =>
    {
        CommonTracingBuilder.ConfigureTracing(
            tracerProviderBuilder,
            builder.Configuration,
            "platformui",   // service name
            "frontend");    // service namespace

        tracerProviderBuilder
            .AddAspNetCoreInstrumentation()
            .AddHttpClientInstrumentation()
            .AddSqlClientInstrumentation();
    })
    .WithMetrics(meterProviderBuilder =>
    {
        CommonMetricsBuilder.ConfigureMetrics(
            meterProviderBuilder,
            builder.Configuration,
            "platformui",
            "frontend");

        meterProviderBuilder
            .AddAspNetCoreInstrumentation()
            .AddHttpClientInstrumentation()
            .AddRuntimeInstrumentation()
            .AddMeter("Secure.Search");
    });
```

For Hatr (SystemTasks / UserTasks / DotNetApi), all signals are configured in `HatrStartup.AddOpenTelemetry()` — all three projects inherit automatically. The `.UseFunctionsWorkerDefaults()` extension (from `Microsoft.Azure.Functions.Worker.OpenTelemetry`) creates a root `Activity` for every function invocation with `faas.trigger` and `faas.execution` attributes, so all downstream HTTP/SQL/Redis spans and `Log.cs` calls inherit the trace context. Without this, function invocations would emit orphan child spans and `Log.cs` entries without a `TraceId`.

Redis instrumentation is activated by passing the `IConnectionMultiplexer` instance to `.AddRedisInstrumentation(connectionMultiplexer)` on the `TracerProviderBuilder`. Pass the instance rather than relying on DI resolution — in Hatr and PlatformUI the multiplexer comes from the static `Sysrepublic.Foundation.Dependencies.Dependency` container, and in ControlPanel it is created at startup when `EnableRedis=True`.

---

## Logging, Tracing, Metrics, and Observability · Resource Attributes
_chunk 498 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

All telemetry carries these OTel resource attributes:

| Attribute | Example (local) | Example (deployed) | Purpose |
|---|---|---|---|
| `service.name` | `platformui` | `platformui` | Identifies the application |
| `service.namespace` | `frontend` | `frontend` | Groups apps by tier (frontend/backend) |
| `deployment.environment` | `local` | `dev-wus2-showcase` | Environment + region + slot |
| `service.version` | `1.0.0.0` | `1.0.0.0` | Assembly version |
| `service.instance.id` | — | Azure instance ID | Unique host instance |
| `grafana_host_id` | — | Azure instance ID | Required by Grafana for host billing |
| `AzureDeploymentSlot` | — | `showcase` | Azure slot name |
| `AzureAppName` | — | `web-dev-wus2-arp-secure` | Azure App Service name |
| `EntryAssemblyName` | `PlatformUI` | `PlatformUI` | .NET assembly name |

The Grafana `job` label is composed as `service.namespace/service.name` (e.g. `frontend/platformui`). Use `deployment.environment` to filter by environment in Grafana dashboards.

The `deployment.environment` is composed from Azure config: `{AzureEnvironment}-{AzureRegion}-{DeploymentSlot}`. Falls back to `local` for local development.

---

## Logging, Tracing, Metrics, and Observability · Custom Metrics
_chunk 499 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

### Search Metrics (ENG-2645)

`SearchAccess.ExecuteQuery()` emits custom OTel metrics via the `Secure.Search` meter:

| Metric | Type | Unit | Description |
|---|---|---|---|
| `secure.search.executed` | Counter | `{searches}` | Total searches executed |
| `secure.search.duration` | Histogram | `ms` | Total search duration (wall clock) |
| `secure.search.provider_duration` | Histogram | `ms` | DB provider execution time |
| `secure.search.result_count` | Histogram | `{rows}` | Number of rows returned |

Attributes on all search metrics:

| Attribute | Values | Description |
|---|---|---|
| `search.success` | `true` / `false` | Whether the search succeeded |
| `search.area` | e.g. `Transactions`, `CashierProfile` | Search category |
| `search.requester` | `SearchResults`, `DashboardGrid`, `DashboardChart`, `DashboardInfoTile`, `PowerBiExport` | What initiated the search |
| `search.from_cache` | `true` / `false` | Whether results came from cache |
| `search.connection` | e.g. `application-direct`, `pos-data` | Database connection name |

### Runtime Metrics

All apps emit .NET runtime metrics via `AddRuntimeInstrumentation()`:
- `process.runtime.dotnet.gc.*` — garbage collection
- `process.runtime.dotnet.thread_pool.*` — thread pool
- `process.threads` — thread count

### ASP.NET Core Metrics

Frontend apps emit HTTP request metrics via `AddAspNetCoreInstrumentation()`:
- `http.server.request.duration` — RED metrics (rate, errors, duration)

---

## Logging, Tracing, Metrics, and Observability · DB Health Checks (ENG-2646)
_chunk 500 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

PlatformUI exposes ASP.NET Core health checks at `/health/db` for all database connections defined in `CoreConnections.cs`.

Each connection is checked by executing `[secure].[HealthCheck]` (a `SELECT 1` sproc). Health checks are registered dynamically via `DatabaseHealthCheckRegistration.AddDatabaseHealthChecks()`.

The existing monitoring endpoints under `/monitoring/api/v1/healthCheck/` are unchanged.

---

## Logging, Tracing, Metrics, and Observability · Pipeline: Application to Storage
_chunk 501 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

```
Application (.NET / Python)
    |
    v
OTEL Collector (batching + common attributes)
    |
    +---> Azure Blob Storage   (long-term retention, protobuf format)
    +---> New Relic             (short-term retention + alerting, OTLP over HTTP)
    +---> Grafana Cloud         (POC — traces, logs, metrics via OTLP/HTTP)
    +---> Snowflake via EventHub (WIP)
```

All three signals (logs, traces, metrics) flow through the same collector pipeline.

### Endpoint Resolution

The builders resolve the OTLP endpoint in this order:

1. `OTEL_EXPORTER_OTLP_ENDPOINT` — standard env var, used for local dev (Aspire Dashboard, Rider OTel plugin)
2. `OTEL_COLLECTOR_OTLP_{SIGNAL}_ENDPOINT` — signal-specific (e.g. `OTEL_COLLECTOR_OTLP_LOGS_ENDPOINT`)
3. `OTEL_COLLECTOR_OTLP_ENDPOINT` — generic base URL; signal path (`/v1/traces`, `/v1/logs`, `/v1/metrics`) is appended automatically
4. Fallback: `http://HOST_MACHINE:4318` (local) or `http://otel-collector:4318` (deployed)

In deployed environments, `OTEL_COLLECTOR_OTLP_ENDPOINT` is set via the `SetSlotConfiguration.yaml` pipeline template to the collector's App Service URL.

### OTEL Collector

Collector configs live in `docker/opentelemetry-collector/`:

| Config file | Purpose |
|---|---|
| `otel-collector-config.hatr.yaml` | Production — New Relic + file export |
| `otel-collector-config.grafana-poc.yaml` | Grafana POC — New Relic + Grafana Cloud + file export |
| `otel-collector-config.grafana-local.yaml` | Local dev — routes to local Tempo/Loki/Mimir |
| `otel-collector-config.local.yaml` | Local dev (legacy) — file + console export |

The collector:
1. Receives telemetry (logs, traces, metrics) from applications via OTLP HTTP
2. Batches them
3. Adds environment-level attributes (collector instance ID)
4. Exports to configured destinations

### Grafana Cloud Export

The `grafana-poc` config adds an `otlphttp/grafana` exporter alongside the existing New Relic export. Required env vars on the collector:

| Variable | Purpose |
|---|---|
| `GRAFANA_CLOUD_OTLP_ENDPOINT` | Grafana Cloud OTLP gateway (e.g. `https://otlp-gateway-prod-us-west-0.grafana.net/otlp`) |
| `GRAFANA_CLOUD_AUTH` | Base64-encoded `instance_id:api_token` |

The Grafana config is enabled per-environment via the `collectorConfigFile` parameter in the collector deployment template (`DeployOpenTelemetryCollector.yaml`).

---

## Logging, Tracing, Metrics, and Observability · Local Development
_chunk 502 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

### Local Grafana Stack

For viewing traces, logs, and metrics locally, use the Grafana observability stack:

```bash
docker compose -f docker-compose.grafana.yml up -d
```

Grafana UI: `http://localhost:3000` (anonymous admin, no login required)

The stack includes:

| Service | Role | Internal Port |
|---|---|---|
| OTEL Collector | Receives OTLP, routes to backends | 4317 (gRPC), 4318 (HTTP) |
| Tempo | Trace storage | 3200 |
| Loki | Log storage | 3100 |
| Mimir | Metric storage | 9009 |
| Grafana | Dashboards and exploration | 3000 |

Data sources (Tempo, Loki, Mimir) are auto-provisioned — no manual setup needed.

The run configurations (`.run.xml`) for PlatformUI, System Tasks, and User Tasks set `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318` to send telemetry to the collector (same endpoint as the previous Aspire Dashboard setup).

To reset all stored telemetry data:

```bash
docker compose -f docker-compose.grafana.yml down -v
```

---

## Logging, Tracing, Metrics, and Observability · Querying Telemetry
_chunk 503 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/observability.md_

### New Relic (cloud environments)

Use **Query your Data** in New Relic with NRQL. Always specify `SINCE` or results default to the last 30 minutes.

| Environment | Account |
|---|---|
| Prod (US, EU) | Retail PROD |
| Non-prod | Retail Non-Prod + Secure |

### Grafana Cloud (POC)

Traces, logs, and metrics are available in Grafana Cloud:
- **Application Observability** — service inventory, RED metrics, service maps (filter by `deployment_environment`)
- **Explore > Tempo** — trace search
- **Explore > Loki** — log search
- **Explore > Mimir** — metric queries (PromQL)

### On-prem / Legacy

On-prem logs are stored in the platform database. Three tables:

| Table | Purpose |
|---|---|
| `LogRecord` | First occurrence of a log (message, host, service, hash) |
| `LogOccurrence` | Deduplicated subsequent occurrences (matched by hash) |
| `LogAttribute` | Structured attributes (component, severity, clientID, etc.) |

Query via the `arp.LogRecordView` view, which joins occurrences with common attributes for filtering.

The OTEL Forwarder reads rotated protobuf log files from the collector output directory, bulk-inserts to the DB, compresses and archives to `\\<ENV>\\OTEL\\Logs\\Archive`. Retention is configurable via environment variables on the forwarder task group.

- DB retention: pruned after 1 week
- Disk archive retention: pruned after 1 year

## Other Data Stores · Overview
_chunk 504 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/other.md_

Not all of Secure's data lives in SQL MI or the analytics warehouse. A couple of features use purpose-specific stores:

- **AI Outliers** caches ML results in Azure Table Storage
- **ORC case linking** uses Azure AI Search as a vector + full-text index

---

## Other Data Stores · AI Outliers — Azure Table Storage
_chunk 505 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/other.md_

AI Outliers runs its IsolationForest model in a Python Azure Functions app and keeps two kinds of table in Azure Table Storage: a **per-run results table** for each analysis, plus a single **status table** that tracks the lifecycle of every analysis request in the slot. The .NET side (work item generator, profile pages) reads back via the Python API, which reads from both tables.

### Per-run results table

One table per analysis request, named from the request parameters:

```
{environment}c{client_id}kt{key_type}pt{period_type}{year}{period}md5{hash}
```

Contents:

| Row | Purpose |
|---|---|
| `__response` row | Overall analysis metadata for this run |
| Per-entity rows (one per store/cashier) | SHAP values, anomaly score, status (red/amber/green) |

The red/amber/green status here is a percentile-based classification of each entity: amber = top X% of scores, red = top X/10%. See `SecureAI.OutlierBoundaryPercent` config item.

### Status table

One table per deployment slot, shared across all clients and all requests:

```
{deploymentSlot}AiOutlierStatus
```

It tracks where each analysis request is in its lifecycle — used to decide whether to return cached results, re-queue a run, or surface an in-progress/error state to the caller.

| Column | Purpose |
|---|---|
| `PartitionKey` / `RowKey` | Same hashed partition / row keys as the results table, so requests line up 1:1 |
| `data` | JSON snapshot of the original `SecureAIRequest` (for re-running) |
| `status` | `None` (just enqueued), `complete`, `error`, or `invalidated` |

Flow (`azure_table_utils.get_response`):

1. Look up the status row for the incoming request.
2. No row → `log_row(req)` writes a `None`-status row and enqueues a message on `{deploymentSlot}-ai-outlier-queue`; returns `AIJobNotRunYet`.
3. Status `invalidated` → same as missing — re-enqueue and return `AIJobNotRunYet`.
4. Status is a non-terminal value (anything other than `complete`, `None`, or `error`) → surface it directly as an error.
5. Otherwise read the `__response` row from the per-run results table.

`invalidate_status_row(req)` flips a completed run's status to `invalidated` — used when upstream data changes and the cached results should no longer be trusted. The next call to `get_response` will re-queue.

### Where it's written / read

- **Written by** the Python API (`Sources/PythonApi/ai_outliers/azure_table_utils.py`)
- **Read by** the same API when `.NET` code (`SecureAiOutlierAnalysisApiClient`) asks for results

See [AI Outliers](../features/ai-outliers.md) for the full architecture.

---

## Other Data Stores · ORC Case Linking — Azure AI Search
_chunk 506 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/other.md_

Secure ORC can recommend other cases that might be linked to the one an investigator is working on. Recommendations run against an Azure AI Search service (formerly Azure Cognitive Search) that holds vector embeddings for semantic similarity and Lucene full-text indexes for the incident search screens.

ORC was originally a separate Python Azure Functions app with one function deployment per tenant. It was ported to Azure Functions and reworked for multi-tenancy in PR 47516, then further tightened in PR 49790 — the indexing work now runs inside Secure's own HATR system/user tasks, and index resolution goes through the shared Platform database.

### Azure AI Search service

One AI Search service per environment/region, not per tenant. For example, dev US West 2 is `vss-dev-wus2-arp` in resource group `rg-dev-wus2-arp-appdata`. All clients' indexes live inside this shared service.

### Indexes per client

Two indexes per client, created on tenant onboarding:

| Index | Default name | Purpose |
|---|---|---|
| Recommendation | `{clientId}-recommendations` | Semantic search — vector embeddings of narrative/suspect fields, used to surface potentially-linked cases |
| Search | `{clientId}-search` | Full-text search — powers the incident search screens in the ORC UI via Lucene |

### Local-dev index isolation

When `GlobalConfiguration.EnvironmentName == "local"`, the `RecommendationAddClientActivity` prefixes both index names with the developer's sanitised machine name so multiple devs can share the dev AI Search service without clashing:

```
{machineName}-{clientId}-recommendations
{machineName}-{clientId}-search
```

The machine name is lower-cased and any character outside `[a-z0-9-]` becomes a `-`, with leading/trailing hyphens trimmed. If the sanitised name ends up empty, `local` is used as a fallback.

Source: `Sources/Hatr/ApprissRetail.Secure.Hatr.SystemTasks/RecommendationIndex/RecommendationAddClientActivity.cs`.

### Vectorised fields

The following fields are vectorised (via Azure OpenAI embeddings) and searchable in the recommendation index:

- Overview
- Attire
- Report Narrative
- Identifying feature
- `vother` (vehicle free-text)

Additional fields are indexed as plain text on the same index and queryable via Lucene full-text syntax.

### Semantic vs matching search

Both flavours return scores as floats; minimum thresholds come from the request or from the tenant's per-client `TenantSearchInformation` row.

- **Semantic search** — embed the query, cosine-similarity against the recommendation index vectors, return highest certainties.
- **Matching search** — SQL-based. First a bi-gram filter on first/last name, then n-gram matching on a larger field set, with scoring.

A combined mode uses both, normalising the raw Lucene score (unbounded) against the 0–1 vector-similarity range via `SearchScoreNormalisation`.

### `TenantSearchInformation`

Per-client, per-search-type configuration, written on tenant onboarding and read on every indexing task and recommendation request. Lives in the Platform database (accessed via `IIncidentService.GetTenantSearchInformation(searchType)`).

There is **one row per search type per client**, keyed by `SearchType`:

| SearchType | What it configures |
|---|---|
| `recommendation` | The recommendation (semantic) index |
| `search` | The search (full-text) index |

Fields set at creation (`RecommendationAddClientActivity`):

| Field | Default | Purpose |
|---|---|---|
| `IndexName` | `{clientId}-recommendations` / `{clientId}-search` (or machine-prefixed locally) | The AI Search index name to target — decoupled from code deploy so the index can be swapped without redeploying |
| `SearchType` | `recommendation` or `search` | Which index this row configures |
| `SearchScoreNormalisation` | `250` | Divisor for the raw Lucene score when combining with the 0–1 vector similarity |
| `Certainty` | `2.0` | Minimum score threshold for returned results |

If `IndexName` is set on a row, it overrides the default. There's a safety check in `IncidentRecommendationService` (and the re-index activities) that only honours an override if it still starts with `{clientId}-` — clients can't accidentally read another tenant's index.

### Indexing tasks (HATR)

Indexing is done by three HATR activities, not by an Azure SQL trigger as in the pre-47516 world:

| Activity | Role | Source |
|---|---|---|

## Other Data Stores · ORC Case Linking — Azure AI Search (cont. 2)
_chunk 507 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/other.md_

| `RecommendationAddClientActivity` | Tenant onboarding — creates both indexes and the `TenantSearchInformation` rows | `Sources/Hatr/ApprissRetail.Secure.Hatr.SystemTasks/RecommendationIndex/` |
| `RecommendationReIndexClientActivity` | Bulk re-index of all a client's suspects/search documents in batches | Same folder |
| `RecommendationIndexingActivity` | Single-record indexing — by master case, shoplifting, suspect, or vehicle ID | `Sources/Hatr/ApprissRetail.Secure.Hatr.UserTasks/RecommendationIndexing/` |

All three resolve the target index names from `TenantSearchInformation`, falling back to the `{clientId}-recommendations` / `{clientId}-search` defaults if no override is set.

### At query time

`PlatformUI.Areas.Orc.Core.Recommendation.IncidentRecommendationService` (`Sources/UI/PlatformUI/Areas/Orc/Core/Recommendation/IncidentRecommendationService.cs`) reads the recommendation index on each request. It uses the same resolution — default `{clientId}-recommendations`, overridden by `TenantSearchInformation` if the override name starts with `{clientId}-`.

---

*Back: [Database Architecture](../databases.md)*

## What Appriss Retail Does · Overview
_chunk 508 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/overview.md_

Appriss Retail builds software that helps retailers find and stop loss. Loss in retail means anything that reduces profit without a sale — cashier fraud, organised retail crime, returns abuse, operational errors, and vendor theft. Left unchecked, these eat 1–3% of revenue across a typical retailer.

Our platform sits between the retailer's raw transaction data and their loss prevention teams. We ingest every transaction — every POS receipt, return, refund, void, and override — and turn it into a searchable, analysable record. Analysts build searches (queries) over that data to surface exceptions: transactions that look suspicious. Investigators follow up on the exceptions. Store managers see dashboards relevant to their location. Executives see the big picture.

## What Appriss Retail Does · What we are not
_chunk 509 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/overview.md_

We are not a CCTV or physical security company, though we integrate with CCTV vendors. We are not a general-purpose BI tool, though we have dashboard and reporting features. We are not a point-of-sale system — we consume POS data, we do not produce it.

## What Appriss Retail Does · Scale and reach
_chunk 510 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/overview.md_

We serve large multi-site retailers globally, with deployments in both US and EU regions. Customers range from grocery and general merchandise chains to specialty retail. The platform processes hundreds of millions of transactions across thousands of locations per customer.

## What Appriss Retail Does · The business model
_chunk 511 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/overview.md_

Customers pay a subscription. The platform is multi-tenant — each customer has their own isolated data schema but shares the application infrastructure. Configuration (which features are enabled, how searches are defined, what the location hierarchy looks like) is specific to each customer and lives in a git repository called **arpfiles**.

---

*Next: [Clients](clients.md) · [Departments](departments.md) · [Personas](personas.md)*

## Reference Data · Overview
_chunk 512 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

**Reference data** is the slow-moving, lookup-style data that every other part of the platform joins against: stores, employees, products, calendars, timezones, CCTV cameras, enumerations (case classes, field definitions, transaction types). Distinct from **transactional data** (POS events in the Transaction Vault) and from **user data** (tenant-uploaded CSVs).

Reference data is per-tenant. It lives in a dedicated per-tenant Reference database on SQL MI and is mirrored into ARDM (Snowflake / Greenplum) so searches can join it efficiently without crossing engines.

---

## Reference Data · What counts as reference data
_chunk 513 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

| Area | Contents |
|---|---|
| Locations | Stores, store attributes, geo, hierarchy (see `hierarchy-generation.md`) |
| Employees | Roster, clocked hours, scheduled hours, operator roles |
| Products | SKUs, UPCs, pricing, vendor relationships, product hierarchy |
| Calendars | Business periods (daily, weekly, monthly), nested period structures |
| Timezones | Per-location time zone for camera/event correlation |
| CCTV cameras | Camera references per location |
| Enumerations | Category lookups: transaction types, case classes, field definitions, tender types — per-culture display values |
| Promotions, vendors | Product-related reference lists |

**Not reference data:**
- Transactional data (POS events, receipts) — see `transaction-vault.md`.
- User data (CSVs uploaded through the UI, materialised as JSONB rows in ARDM) — see `user-data.md`.

---

## Reference Data · Storage
_chunk 514 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

### Per-tenant Reference DB (SQL MI)

Each tenant has a dedicated Reference database on Azure SQL MI alongside its Platform DB. Naming follows the standard SQL MI convention:

```
sqldb-{env}-{region}-arp-{slot}-{paddedClientId}-{abbr}-reference
```

Example: `sqldb-prd-wus2-arp-production-001-astromart-reference`.

The EF Core context and models:

| File | Purpose |
|---|---|
| `Sources/Databases/Reference/Reference.Core/ReferenceCoreContext.cs` | EF Core context — 19 DbSets covering the areas above |
| `Sources/Databases/Common.Models/ApprissRetail.Secure.Common.Models/SecureEnumerationReferenceData.cs` | Enumeration model (categories, culture-aware labels, sort order) |
| `Sources/Databases/Common.Models/ApprissRetail.Secure.Common.Models/ReferenceTimezone.cs` | Timezone model |
| `Sources/Databases/Common.Models/ApprissRetail.Secure.Common.Models/CctvCameraReference.cs` | Camera reference model |

The Reference DB is authoritative for MSSQL queries. ARDM reference tables (`reference_location`, `reference_employee`, etc.) are DataOps-maintained copies.

### ARDM reference tables

Searches running in Snowflake/Greenplum join against ARDM reference tables (`reference_*`). DataOps loads these tables directly (not through Lunar). YADL copies ARDM reference data into the MSSQL `place.Location` table so MSSQL searches can use it without cross-engine calls.

See `../databases/snowflake.md` and `../data-model.md` for more on the DataOps → ARDM → MSSQL pipeline.

---

## Reference Data · Connections
_chunk 515 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

Reference data is reached via named database connections (see `search.md` for how data areas map to connections):

| Connection | Target | Used by |
|---|---|---|
| `securereferencedata-direct` | Snowflake / Greenplum | ARDM-backed searches joining to `reference_*` tables |
| `securereferencedata-direct-mssql` | SQL MI Reference DB | MSSQL-backed searches and services that hit the Reference DB directly |

---

## Reference Data · Loading and seeding
_chunk 516 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

Reference data arrives by several paths depending on what it is.

### Lunar installer (enumerations, timezones, platform-level lookups)

Seed-style reference data — enumerations, transaction type lists, case classes, default field definitions — is seeded via Lunar using **layered** JSON seed files from `arpfiles`:

1. `repo/platform/seed/*.json` — platform-wide defaults
2. `repo/platform/seed/*.{environment}.json` — environment overrides (dev, staging, prod)
3. `repo/{clientId}/seed/*.json` — client-specific customisations
4. `seed-manifest.json` — explicit client definitions

Lunar tracks applied records in `__SeedHistory` so modified rows are not re-seeded. See `../databases/lunar.md` for the full seeding model.

### DataOps (stores, employees, products)

High-volume operational reference data — the store roster, employee roster, product catalogue — is loaded by **DataOps** directly into ARDM `reference_*` tables, typically via sFTP drops or customer feeds. DataOps loads code and description; if only one is provided, both get the same value. DataOps does **not** enforce hierarchy integrity.

### YADL (reference → MSSQL mirror)

YADL copies ARDM reference data into MSSQL `place.Location` (and peers) so MSSQL searches can join locally. This keeps the two engines in sync without requiring every query to cross into ARDM.

> The classic Hierarchy Generation job additionally built strict-tree structure tables from this data — the Square Hierarchy work is removing that job. See `hierarchy-generation.md`.

### HATR reference-data tasks

| Task | Role |
|---|---|
| `ReferenceDataBackLoad` | Re-hydrates reference data when a client is onboarded or refreshed |
| `CctvReferenceDataLoad` | Loads CCTV camera references |

See `../hatr.md`.

---

## Reference Data · Load order
_chunk 517 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

When a client is onboarded, reference data loads **before** transactional data — stores, employees, and products must exist before their IDs show up in POS transactions. This ordering is enforced by the onboarding scripts, not at runtime.

---

## Reference Data · Consumers
_chunk 518 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

Reference data is the join partner for almost everything:

- **Searches** (`search.md`) — every data area joins to one or more reference tables for display labels, hierarchy filtering, and grouping.
- **Work items** (`work-item-generation.md`) — location IDs, cashier IDs, product IDs on work items are all reference-data keys.
- **Reports** (`reports.md`) — aggregations by store, employee, product, period.
- **Incident / Nettrack** — references stores, employees, case classes, field definitions.
- **Dashboards** — slicers (store list, employee list, period picker) are populated from reference data.

---

## Reference Data · Reference DB vs. Platform DB vs. User Data
_chunk 519 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

| Aspect | Reference DB | Platform DB | User Data |
|---|---|---|---|
| **Contents** | Stores, employees, products, enumerations, calendars | Investigations, work items, SSO, dashboards, searches | Tenant-uploaded CSV data |
| **Change rate** | Daily / weekly (customer feeds) | Continuous (per user action) | Ad-hoc on upload |
| **Engine** | SQL MI (+ ARDM mirror) | SQL MI | ARDM (`secure.UserData`, JSONB) |
| **Load path** | Lunar seeding + DataOps + YADL | EF Core migrations + runtime writes | Upload manager |
| **Accessed via** | `securereferencedata-direct[-mssql]` | `application-direct` | JSON-path searches against `secure.UserData` |

---

## Reference Data · Key file pointers
_chunk 520 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

| Concern | File |
|---|---|
| EF Core context for Reference DB | `Sources/Databases/Reference/Reference.Core/ReferenceCoreContext.cs` |
| Enumeration model | `Sources/Databases/Common.Models/ApprissRetail.Secure.Common.Models/SecureEnumerationReferenceData.cs` |
| Timezone model | `Sources/Databases/Common.Models/ApprissRetail.Secure.Common.Models/ReferenceTimezone.cs` |
| CCTV camera model | `Sources/Databases/Common.Models/ApprissRetail.Secure.Common.Models/CctvCameraReference.cs` |
| Lunar seeding | `Sources/Databases/Installer/` |

## Reference Data · Related
_chunk 521 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reference-data.md_

- `../databases.md` — database architecture overview
- `../databases/sql-mi.md` — per-tenant Reference DB naming and structure
- `../databases/snowflake.md` — ARDM reference table layout
- `../databases/lunar.md` — seed layering and `__SeedHistory`
- `../data-model.md` — DataOps and SnowTime pipelines
- `user-data.md` — the other kind of tenant-supplied data
- `hierarchy-generation.md` — the hierarchy layer built on top of location reference data
- `transaction-vault.md` — the transactional side

## Scheduled Reports · Overview
_chunk 522 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

The reporting system generates reports from saved searches on a calendar schedule and distributes them to users via email and in-app notifications. This document covers the scheduled report distribution pipeline.

---

## Scheduled Reports · Overview
_chunk 523 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

```
Report Definitions (repo files)
    ↓
ReportGeneratorTask (HATR, daily 5:30 AM)
    ↓
  GetReportDefinitionsActivity — loads definitions from repo
    ↓
  ReportGeneratorActivity — executes each definition (parallel, max 4)
    ↓
    ReportDefinitionProcessor — runs searches, builds dynoview output
    ↓
    ReportingService — records run, identifies recipients, sends notifications
    ↓
    SendGrid — email delivery
```

---

## Scheduled Reports · HATR Scheduling
_chunk 524 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

The report generator runs as an Azure Durable Functions orchestration.

| Property | Value |
|---|---|
| Task | `ReportGeneratorTask` |
| Schedule | Daily at 5:30 AM |
| Task ID | `47ccb9d1-103d-4e39-b24c-615d1d55ed08` |
| File | `Sources/Hatr/.../ReportGenerator/ReportGeneratorTask.cs` |

The orchestration has two triggers:
- **Scheduled** — daily at 5:30 AM
- **Manual** — on-demand via request trigger

### Activities

1. **GetReportDefinitionsActivity** (`Sources/Hatr/.../ReportGenerator/GetReportDefinitionsActivity.cs`) — loads report definitions from the repo
2. **ReportGeneratorActivity** (`Sources/Hatr/.../ReportGenerator/ReportGeneratorActivity.cs`) — executes individual report definitions

Optional input filters allow targeting specific reports:
- `ReportVfpFilter[]` — limit to specific report definitions
- `CalendarFilter[]` — limit to specific calendars
- `PeriodFilter[]` — limit to specific period types
- `ForceRerun` — re-run already completed reports

---

## Scheduled Reports · Report Definitions
_chunk 525 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

A report definition is a repo file that specifies what data to query and how to present it.

### ReportDefinition Model

`Sources/Core/Core/Report/Models/ReportDefinition.cs`

| Field | Purpose |
|---|---|
| `name`, `description`, `id` | Identification |
| `enabled` | Enable/disable toggle |
| `PoweredBy` | Data source type (see below) |
| `Calendar` | Which calendar drives scheduling |
| `PeriodType` | Day / Month / Quarter / Year |
| `Searches[]` | Search-based data sources (ReportContent) |
| `SendNotification` | Trigger notifications on generation |
| `TeamIds[]` | Distribution groups |

### PoweredBy Types

| Value | Meaning |
|---|---|
| `Nothing` (0) | Static report — no data source |
| `Search` (1) | Driven by search results |
| `Hierarchy` (2) | Driven by hierarchy members — generates one report per member |

### Report Distribution Model

`Sources/Core/Core/Reporting/ReportDistributionModel.cs`

Controls how and to whom reports are sent:
- `emailSubject`, `emailContent` — custom email text
- `distributeTeamIds[]` — team-based distribution
- `allMembers`, `includeHierarchyLevelsBelow` — hierarchy cascade
- `snooze`, `snoozeDayOfWeek`, `snoozeTime` — snooze configuration

Distributions are stored as repo files at `/system/reportmanager/definitions/` with `.reportdist` extension.

---

## Scheduled Reports · Report Generation Pipeline
_chunk 526 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

### ReportDefinitionProcessor

`Sources/Core/Core/Report/Core/ReportDefinitionProcessor.cs`

The core generation engine. For each report-calendar-period combination:

1. Resolves the calendar period using `ExtendedCalendarDefinition`
2. Based on `PoweredBy` type:
   - **Search** — executes the search SSR, applies parameters
   - **Hierarchy** — iterates hierarchy members, generates per member
   - **Nothing** — single static report
3. Builds a dynoview (XML-based rendering template) from `reporttemplate.dynoview`
4. Saves the generated dynoview as a static file in the repo

**Parallelism:** Configurable via `Report.MaxDegreesOfParellelism` (default: 4).

### ReportingService

`Sources/Core/Core/Reporting/ReportingService.cs`

After generation:
1. `InsertReportDistributionRun()` — records the run in the database
2. `GetReportDistributionRunAffectedUsers()` — identifies recipient users
3. Triggers notifications via `NotificationService`
4. `UpdateStatistics()` — logs metrics to `[stats].[Reports]`

### Calendar-Aligned Scheduling

`Sources/Core/Core/Reporting/ReportingCalendarAlignedJobProvider.cs`

Implements `ICalendarAlignedJobProvider` to automatically create/delete report jobs when calendars are created or deleted. The `ExtendedCalendarDefinition` supports:
- `SelectedPeriod` — period type (Day/Month/Quarter/Year)
- `SpecificDaysOfWeek[]` — optional day filtering
- `SpecificHourOfDay` — optional time constraint

---

## Scheduled Reports · Email Delivery
_chunk 527 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

### SendGrid (primary)

`Sources/Core/Core/Mail/Clients/SendGridEmailClient.cs`

- Feature flag: `Feature.EnableEmailSending` (master toggle)
- API key: `SendGrid.ApiKey`
- Supports HTML templates, attachments, reply-to, and priority settings
- Recipients are semicolon-delimited email addresses

### SMTP (legacy, Incident module only)

`Sources/Incident/UI/UI/Server/Services/EmailService.cs`

Falls back to SMTP for the legacy Incident module. Configured via the `Options` entity: `EmailServer`, `EmailPort`, `EmailFromAddress`, `EmailSSL`, `EmailUserName`, `EmailPassword`.

### Notifications

`Sources/Core/Core/Notifications/NotificationService.cs`

In-app notifications are created alongside emails:
- Stored via `[notify].[NotificationInsert]`
- User resolution via `[notify].[SelectUsersForNotifications]`
- Supports escalation timing and location-based distribution

---

## Scheduled Reports · Database Schema
_chunk 528 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

Tables in the `report` schema of the Platform database.

### report.ReportDistribution

| Column | Type | Purpose |
|---|---|---|
| ReportDistributionID | GUID PK | Distribution identifier |
| DisplayName | NVARCHAR(200) | Display name |
| PeriodTypeID | SMALLINT | Period type reference |
| HierarchyID, HierarchyLevel, HierarchyCode | INT/BYTE/NVARCHAR | Hierarchy scope |
| LocationID | BIGINT | Location scope |
| IncludeHierarchyLevelsBelow | BIT | Cascade to child levels |
| Details | NVARCHAR | JSON report configuration |
| Deleted | BIT | Soft delete |

Model: `Sources/Databases/Platform/Models/report/ReportDistribution.cs`

### report.ReportDistributionRuns

| Column | Type | Purpose |
|---|---|---|
| RunID | BIGINT PK | Run identifier |
| ReportDistributionID | GUID FK | Parent distribution |
| RunDateTime | DATETIME | When the report was generated |
| StaticDynoViewVfp | NVARCHAR(440) | Path to generated dynoview |
| PeriodValue, PeriodYear | INT/SMALLINT | Which period was generated |
| SnoozeLocalTime | DATETIME | Snooze until time |

Model: `Sources/Databases/Platform/Models/report/ReportDistributionRuns.cs`

### report.ReportUser / report.ReportTeam

Junction tables for user and team access to report definitions. Composite keys of `DefinitionVirtualFilePath` + `UserID` or `TeamID`.

---

## Scheduled Reports · Key Services
_chunk 529 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

| Service | File | Purpose |
|---|---|---|
| ReportDefinitionProcessor | `Sources/Core/Core/Report/Core/ReportDefinitionProcessor.cs` | Core generation engine |
| ReportingService | `Sources/Core/Core/Reporting/ReportingService.cs` | Run recording, notifications, stats |
| ReportRunService | `Sources/Core/Core/Report/Core/ReportRunService.cs` | Individual run persistence |
| ReportManagerService | `Sources/UI/UI/Areas/ReportManager/Core/ReportManagerService.cs` | UI-facing report configuration |
| ReportLibraryService | `Sources/UI/UI/Areas/ReportManager/Core/ReportLibraryService.cs` | Report browsing and filtering |
| ReportDistributionProcessor | `Sources/Core/Core/Reporting/ReportDistributionProcessor.cs` | Legacy job system executor |

---

## Scheduled Reports · Configuration
_chunk 530 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

| Config Item | Default | Purpose |
|---|---|---|
| `Feature.EnableEmailSending` | true | Master email toggle |
| `SendGrid.ApiKey` | — | SendGrid API credentials |
| `Report.MaxDegreesOfParellelism` | 4 | Parallel report processing threads |
| `Feature.Report.NoResultsNotification` | true | Notify users when report has no results |

---

## Scheduled Reports · Confluence References
_chunk 531 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/reports.md_

- [5.4 Report Distribution](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/1128893056) — user-facing report distribution guide
- [Report Example: Regional Report](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/1128893071) — step-by-step example
- [In House Reporting / Izenda Replacement](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/476053438465) — reporting initiative overview

## Search Service · Overview
_chunk 532 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

A **Search** is the platform's core query primitive. Reports, metrics, work items, dashboards, investigations — all of them ultimately run a search. Everything that presents data in Secure starts here.

The Search Service owns: what queries exist (`Searchable` definitions), what data area they run against (`DataAreaConnection`), how they're executed (`SearchAccess`), and how results are surfaced (sync return, async queue, export to Excel).

---

## Search Service · Anatomy of a search
_chunk 533 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

A search has two parts — a **blueprint** and an **instance**.

### Searchable — the blueprint

A `Searchable` describes the query *shape*: what fields can be filtered on, their labels, allowed operators, default parameters, and which cache items are in play. Searchables are XML files stored in the repo (typically under `/system/searches/`, `/system/workview/searches/`, `/system/metrics/searches/`) and loaded via `SearchesRepo`.

**Key types:**
- `Sources/Core/Core/Search/Contract/Searchable.cs` — blueprint type
- `Sources/Core/Core/Search/Contract/SearchableField.cs` — per-field metadata
- `Sources/Core/Core/Search/Contract/SearchesRepo.cs` — repo-backed loader

### SearchServiceRequest — the instance

A `SearchServiceRequest` (SSR) is a concrete, executable query — the filter conditions, groupings, sort order, display filters the user picked. SSRs are XML-serializable so they can be persisted (saved searches), scheduled (reports, metrics), or passed across services.

**Key types:**
- `Sources/Core/Core/Data/Contract/Search/SearchServiceRequest.cs`

Searches can reference other searches via `ReferencedSearchServiceRequests` — that's how compound queries compose (e.g. a report's parameter search feeds its data search).

---

## Search Service · Data areas
_chunk 534 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

A **DataArea** is a logical data source — "Transactions", "Cashier Profile", "Store Data", etc. Each data area maps to:

- a named database connection (`Connection`) — e.g. `application-direct`, `pos-data`, `securereferencedata-direct`
- a display name for the UI
- a "structure name" used to group searchables that share a shape
- an explorer mode (grid, tree, etc.)
- a `Compose` flag — whether users are allowed to author new searches against it

**Key type:**
- `Sources/Core/Core/Search/Contract/DataAreaConnection.cs`

Data area → connection is how search execution routes to the right database: some areas live in SQL MI (Platform DB), some in Snowflake (ARDM), some in Greenplum (legacy), some in the per-tenant reference DB. The caller never picks a database — the data area does.

---

## Search Service · Execution path
_chunk 535 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

```
UI or scheduled trigger
    ↓
SearchController.Search(...)          Sources/UI/UI/Areas/Cpf/Controllers/SearchController.cs
    ↓
SearchService / AsyncSearchService    Sources/Core/Core/Search/Core/SearchService.cs
    ↓
SearchAccess.Execute(SSR)             Sources/Core/Core/Data/Core/SearchAccess.cs
    ↓
IDatabaseProvider                     (MSSQL / Snowflake / Greenplum provider)
    ↓
DataTable (results) + OTEL metrics
```

`SearchAccess.ExecuteQuery()` is also where custom OTEL metrics are emitted under the `Secure.Search` meter — `secure.search.executed`, `secure.search.duration`, `secure.search.provider_duration`, `secure.search.result_count` — with attributes for `search.area`, `search.requester`, `search.success`, `search.from_cache`, and `search.connection`. See `../observability.md`.

### SQL generation

Between `SearchAccess` and the database provider, the SSR is translated into dialect-specific SQL by a composable generator. The same pipeline runs for every engine; the provider-specific subclasses swap in writers for the clauses that differ.

This section is the short version. For the full architecture — every writer, how the `FunctionFramework` registers and dispatches functions, and how the CTE / JSON / referenced-search / arbitrary-join / metric modules plug in — see [`../sql-generator.md`](../sql-generator.md).

```
SSR
 ↓  SqlGenerator.Generate(ssr, director)
 ↓
SqlGeneratorContext   (state: SSR, Table/Param/GroupBy/OrderBy/DisplayField managers)
 ↓  pipeline of Writers, one per clause
[CustomVariableDeclaration] [SelectFieldsFromPhase] [JoinPhase]
[WherePhase] [GroupByPhase] [HavingPhase] [OrderByPhase]
 ↓
SqlGeneratorResult   ( SQL string + parameter dictionary )
 ↓
DbCommand (ADO.NET)
```

**Key files:**
- `Sources/Core/Core/Data Providers/Sql/Generator/SqlGenerator.cs` — base orchestrator
- `Sources/Core/Core/Data Providers/Sql/Mssql/Generator/MsSqlGenerator.cs` — MSSQL dialect
- `Sources/Core/Core/Data Providers/Sql/Snowflake/Generator/SnowflakeSqlGenerator.cs` — Snowflake dialect
- `Sources/Core/Core/Data Providers/Sql/Postgresql/Generator/PostgresqlGenerator.cs` — Greenplum/Postgres dialect
- `Sources/Core/Core/Data Providers/Sql/Generator/Context/SqlGeneratorContext.cs` — context and phase enum
- `Sources/Core/Core/Data Providers/Sql/Generator/Context/SqlParamManager.cs` — parameter binding
- `Sources/Core/Core/Data Providers/Sql/Generator/Common Writers/Writers/` — `DisplayFieldWriter`, `FromTableWriter`, `JoinedTablesWriter`, `WhereWriter`, `GroupByWriter`, `HavingWriter`, `OrderByWriter`

**What each phase builds:**

| Phase | Source on the SSR | Notes |
|---|---|---|
| SELECT | `DisplayFields` (ordered by `DisplayOrder`) | Dialect writers handle `TOP` (MSSQL) vs `LIMIT` (SF/PG) |
| FROM / JOIN | Data area root table + referenced searches + module-contributed joins | See hierarchy note below |
| WHERE | `MandatoryConditionGroup` + user `ConditionGroup` + `SqlContextModule.GetCustomConditionGroup(ctx)` per registered module | Modules AND their conditions onto the where clause |
| GROUP BY | Aggregated fields and grouping flags on `DisplayField` | |
| HAVING | Post-aggregation conditions | |
| ORDER BY | `DisplayField.SortOrder` + `SortIndex` | MSSQL emits `OFFSET 0 ROWS` + `OPTION(RECOMPILE)` |

**Parameter binding.** All user-supplied values flow through `SqlParamManager` — `AddConstantParameterAndGetName` for scalars, `AddTableParameterAndGetName` for `IN`-style lists. The manager emits stable placeholders (`@p1`, `@p2`, …) and tracks the DbType per parameter so ADO.NET binds them safely. No value ever lands in the raw SQL string, which is the project's SQL-injection guarantee.

**Dialect differences** are confined to the provider subclass overriding specific writers. MSSQL handles JSON/string functions and `TOP`/`OFFSET … FETCH`; Snowflake swaps in `SnowflakeSqlJsonContextModule` for its JSON semantics and uses `LIMIT`; Postgres/Greenplum uses JSONB operators via `PostgresqlJsonContextModule`. Shared clause logic stays in the base writer.

## Search Service · Execution path (cont. 2)
_chunk 536 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

**Modules extend the generator** without touching its core. Registered `SqlContextModule`s contribute custom joins (`WriteCustomJoinsEvent`) and custom where conditions (`GetCustomConditionGroup`). This is where **hierarchy / data-access filtering** is spliced in — the joins against `secure_memberUsers` / `secure_locationUsers` (or the Square Hierarchy equivalents) are injected here, not hard-coded in `WhereWriter`. See `location-hierarchy.md`. `ReferenceSearchModule` handles joining in referenced searches the same way.

**Output.** `SqlGeneratorResult` bundles the final SQL string with the parameter dictionary, cached by `DbCommonDataProviderCommandCache` so repeat executions with different parameter values reuse the same compiled SQL.

### DB join vs. in-memory join

A search can pull from one data area or weave together several via referenced searches. The first decision `SearchAccess` makes is whether the whole thing can collapse into a single SQL statement or whether the pieces must run as separate queries and be joined in application memory.

The decision lives in `SearchAccess.cs`, around the `needToUseInMemoryJoins` check:

```csharp
if (searchServiceRequest.DoesSearchUseReferencedSearches(director))
{
    needToUseInMemoryJoins =
        searchServiceRequest.DoesSearchUseReferencedSearchesWithRelatedFields()
        || !SearchJoinHelper.AreAllLinkedSearchesFromSameDataProvider(searchServiceRequest, director);
}
```

**Rule:**

| Condition | Execution |
|---|---|
| Every linked search (referenced, based-upon, inline `GetReader`) resolves to the same database (server + type; for Postgres, also same DB name) **and** no RelatedFields are used | Single SQL statement — referenced searches become subqueries/CTEs |
| Any linked search uses a different connection, or any RelatedFields are in play | In-memory join — two or more queries, results stitched in the app |

The connection-compatibility check lives in `ConnectionsService.AreConnectionsFromSameDatabase` and is wrapped by `SearchJoinHelper.CanSearchesBeJoinedTogetherInSql` / `AreAllLinkedSearchesFromSameDataProvider`. User-data searches are treated as always joinable (since they're materialised into whichever engine the parent runs against), and — under a feature flag — reference-data searches can be "upgraded" to the Platform connection so they become SQL-joinable.

**DB path** — `ReferenceSearchModule` (a `SqlContextModule`) contributes the subqueries and JOIN clauses during SQL generation. One trip to the database, one cached `DbCommand`.

**In-memory path** — `SearchAccess.ExecuteSearchWithInMemoryJoins` splits execution in two:

1. **Phase one** runs the main search with only its non-referenced display fields and non-referenced conditions.
2. **Phase two** hands the phase-one results to the Evaluation Engine (below), which runs the referenced searches in parallel and stitches everything together in memory.

**Key files:**
- `Sources/Core/Core/Data/Core/SearchAccess.cs` — decision + orchestration of both paths
- `Sources/Core/Core/Data/Contract/Search/SearchJoinHelper.cs` — compatibility rules
- `Sources/Core/Core/Configuration/Core/ConnectionsService.cs` — `AreConnectionsFromSameDatabase`
- `Sources/Core/Core/Data Providers/Sql/Generator/Modules/ReferenceSearch/ReferenceSearchModule.cs` — DB-side joining

### Evaluation Engine

When the in-memory path wins, execution hands off to the **Evaluation Engine** — a staged in-process pipeline that applies conditions, joins referenced searches, groups, picks display fields, and sorts entirely over in-process readers. Full details in [`../sql-generator/evaluation-engine.md`](../sql-generator/evaluation-engine.md).

### Sync vs. async

Short, interactive searches return synchronously via `SearchService`. Anything that might take a while (large exports, scheduled runs) goes through `AsyncSearchService`, which enqueues a HATR `AsyncSearch` user task and returns a handle the UI polls — see `../hatr.md`.

### Caching

Search results are cached per-tenant keyed by search hash + parameters. Implementation lives in `Sources/Core/Core/Data/Cache/SearchCacheService.cs` (wraps the platform cache from `../cache.md`). Cache hits are tagged with `search.from_cache=true` on the metric so hit rate is queryable.

---

## Search Service · How other features plug in
_chunk 537 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

### Reports
`ReportDefinition` bundles one or more searches (`ReportContent`), plus a parameter search for runtime inputs. `ReportDefinitionProcessor` executes them in order and assembles the output.

Key file: `Sources/Core/Core/Report/Core/ReportDefinitionProcessor.cs`. See `reports.md`.

### Metrics
Metric definitions each point at a Searchable + grouping. `MetricCalculatorJob` groups metric definitions by their source search (VFP), executes the search **once**, and reuses the result set to calculate every metric that depends on it. This is where the "search is the unit of data" framing really pays off — the aggregation cost is paid once per period.

Key file: `Sources/Core/Core/Metrics/MetricCalculatorJob.cs`. See `metric-generation.md`.

### Work items
Work item generation runs two searches per definition per period:

1. A **trigger search** (Step 2) finds matching groups/rows — executed via `WorkItemDefinitionProcessor`.
2. A **deaggregation search** (Step 3) runs per row to gather the underlying transaction IDs — executed via `WorkItemDeaggregationProcessor`.

See `work-item-generation.md`.

### Dashboards
React dashboard tiles call back to `SearchController` to render grids, charts, and info tiles. The shared React components live under `Sources/UI/Components/src/_react/src/shared/components/` (queued-search, search-chart, search-data-grid).

---

## Search Service · UI
_chunk 538 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

- **AngularJS composer (CPF)** — `Sources/UI/UI/Areas/Cpf/Views/Search/` is the classic search builder where users pick a data area, add conditions, group/sort, and run or save.
- **React micro-apps** — newer apps consume searches via the shared components (`queued-search`, `search-data-grid`, `search-chart`). They post an SSR to the controller and render the returned DataTable.
- **Export paths** — Excel export runs through `SearchService`; larger or scheduled exports go through the async queue.

---

## Search Service · Hierarchy filtering
_chunk 539 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

Row-level data-access (which stores a user can see) is applied *inside* search execution. When a user's session carries hierarchy restrictions, the generated SQL includes a CTE/join against `secure_memberUsers` / `secure_locationUsers` (ARDM) or the equivalent MSSQL tables to filter rows. The Square Hierarchy work changes this join target — see `hierarchy-generation.md`.

---

## Search Service · Key file pointers
_chunk 540 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

| Concern | File |
|---|---|
| Blueprint model | `Sources/Core/Core/Search/Contract/Searchable.cs` |
| Executable request | `Sources/Core/Core/Data/Contract/Search/SearchServiceRequest.cs` |
| Data area mapping | `Sources/Core/Core/Search/Contract/DataAreaConnection.cs` |
| Repo-backed loader | `Sources/Core/Core/Search/Contract/SearchesRepo.cs` |
| Service layer | `Sources/Core/Core/Search/Core/SearchService.cs` |
| Async queue | `Sources/Core/Core/Search/Core/AsyncSearchService.cs` |
| Execution | `Sources/Core/Core/Data/Core/SearchAccess.cs` |
| Join strategy rules | `Sources/Core/Core/Data/Contract/Search/SearchJoinHelper.cs` |
| Connection compatibility | `Sources/Core/Core/Configuration/Core/ConnectionsService.cs` |
| SQL generator (base) | `Sources/Core/Core/Data Providers/Sql/Generator/SqlGenerator.cs` |
| SQL generator (MSSQL / Snowflake / PG) | `Sources/Core/Core/Data Providers/Sql/{Mssql,Snowflake,Postgresql}/Generator/` |
| Parameter binding | `Sources/Core/Core/Data Providers/Sql/Generator/Context/SqlParamManager.cs` |
| Referenced-search SQL joiner | `Sources/Core/Core/Data Providers/Sql/Generator/Modules/ReferenceSearch/ReferenceSearchModule.cs` |
| Evaluation Engine | `Sources/Core/Core/EvaluationEngine/EvaluationEngine.cs` |
| In-memory join stage | `Sources/Core/Core/EvaluationEngine/Resolver/JoinStage.cs` |
| Cache | `Sources/Core/Core/Data/Cache/SearchCacheService.cs` |
| UI controller | `Sources/UI/UI/Areas/Cpf/Controllers/SearchController.cs` |

## Search Service · Related
_chunk 541 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/search.md_

- `../sql-generator.md` — the full SQL generator (writers, FunctionFramework, modules, evaluation engine)
- `../observability.md` — custom `Secure.Search` OTEL metrics emitted from `SearchAccess`
- `../cache.md` — the platform cache used by `SearchCacheService`
- `../hatr.md` — the `AsyncSearch` user task
- `work-item-generation.md`, `metric-generation.md`, `reports.md` — downstream consumers
- `location-hierarchy.md` — hierarchy filtering joins applied during search execution

## Secure · Overview
_chunk 542 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

Secure is an omnichannel exception-based reporting (EBR) and loss prevention platform. At its core, Secure lets analysts write queries over retail transaction data and automates the surfacing of anomalies to the right people.

The name "Secure" refers to the whole application — it is not just the EBR component. Historically the product had separate names for separate modules (LPMS for incident management, CAMS for audit), but everything is converging under the Secure umbrella as part of Platform Unification.

![Secure Application Suite](secure-apps.png)

## Secure · The core loop
_chunk 543 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

```text
Data Load → Search Definition → Work Item Schedule → Work Item Queue → Investigation → Case
```

1. **Data Load** — Transaction data (POS receipts, returns, voids, employee data, location hierarchy) is ingested from the retailer via SFTP or AR Gateway into the ARDM.
2. **Search** — An analyst writes a search: a query against one or more data areas (transaction types). A search says "find me all transactions matching these conditions."
3. **Work Item Definition** — The analyst turns a search into a scheduled work item definition. The system runs the search on a schedule and creates work items (essentially flagged results) automatically.
4. **Work Item Queue** — Investigators see their assigned work items. Each item links directly to the underlying transactions.
5. **Investigation** — The investigator reviews the evidence, watches linked CCTV footage, and either closes the item or escalates it.
6. **Case** — Significant findings are recorded as cases in Secure Incident for tracking and reporting.

## Secure · Searches
_chunk 544 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

A **search** is the fundamental building block of Secure. Everything — work items, reports, metrics, dashboards, exports — starts with a search.

A search is a query against a **data area**. A data area is a category of retail data: POS transactions, returns, employee records, inventory, and so on. When an analyst builds a search, they are asking: *"Show me all records in this data area that match these conditions."*

Once you have a search, you can do six things with it:

![Search Actions](search-actions.svg)

| Action | What it does |
|---|---|
| **Work Item** | Schedule the search to run automatically and push results into an investigator's queue |
| **Report** | Include it in a scheduled report emailed to users across the organisation |
| **Quick Link** | Surface it as a parameterised shortcut — users can run it ad hoc with their own inputs |
| **Metric** | Record a KPI value on a regular schedule and store it over time for trend analysis |
| **Export** | Send the results to Excel or Power BI, on a schedule or on demand |
| **Ad hoc** | Run it once, right now, and review the results directly |

This is why understanding searches is more important than understanding any individual module. When you are building a new feature — whether it is a dashboard widget, a notification, or an AI-generated work item — you are almost always building something that consumes or produces a search result.

As an engineer, searches surface in:
- The **Search Service** — the backend that executes queries against the ARDM
- **Work Item Generation** — the job that schedules searches and creates work items from results
- **Search Composer** — the UI where analysts build and edit searches

## Secure · Modules
_chunk 545 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

### Exception Based Reporting (EBR)

The original and central module. Covers POS transactions, SCO (self-checkout), online, curbside, DSD (direct store delivery), and cash over/short. Analysts build searches across all these data areas. The transaction viewer provides a receipt-level view with CCTV integration.

### Secure Incident (formerly LPMS)

Incident and case management. When an investigation surfaces a confirmed loss event — theft, fraud, an operational issue — it becomes an incident. Incidents are categorised (policy violation, fraud, training issue, etc.), tracked through resolution, and reportable. BOLOs (Be On the Lookout) allow investigators to share alerts across teams.

### Audit (formerly CAMS)

Audit scheduling and scoring. Store managers and district teams are assigned audits on a schedule. Audit results are scored and feed into dashboards.

### Quick Entry

A stripped-down mobile-friendly interface for store staff to submit incidents and complete audits without needing full Secure access. Analysts configure which forms are Quick Entry enabled.

### AI Outliers

Machine learning model that identifies anomalous cashier and store behaviour. The model runs on metric data — not raw transactions — so no PII is involved. Outlier results surface as work items in the standard queue. Metrics used in the outlier analysis are configurable in Metrics Manager.

The model is fit on Walmart data. "Accuracy" in the traditional ML sense is not the right frame here — the point is outlier detection, not classification.

### Engage Insights

The admin portal for the Engage product. Retailers use Engage Insights to configure how Engage works and view the value they're getting from return authorization.

**Main sections:**

| Section | Purpose |
|---|---|
| Engage Insights Homepage | Customer value metrics, high-level analysis |
| Engage Metrics | Deeper detailed metricsNO  (Return Auth, Claims Auth, Incent) |
| Consumer Profile | View individual consumer details, identity graph, transaction history |
| Task Center | Flagged Receipts, Flagged Consumers, SKU-based Policies, Alert rules |

**Architecture:**
- **React apps**: `engage-portal` (homepage), `engage-metrics`, `engage-consumer-profile`, `engage-task-center`
- **Backend Areas**: `Engage`, `EngageMetrics`, `EngageInsights`, `TaskCenter` (in PlatformUI)
- **Data layer**: Snowflake sprocs in `Sources/Databases/Snowflake/Programmability/Snowflake/EngageDependent/`

Key Snowflake functions:
- `engage_insights__*` — Homepage metrics (engage_value, returns, data_health, top_skus, etc.)
- `engage_metrics__*` — Detailed metrics (core_metrics, time_series)
- `engage_consumer__*` — Consumer profile data (search, id_graph, transactions, stores)

### Sidekick

An AI assistant embedded in the Secure platform, powered by **Anthropic Claude** (claude-sonnet-4-6 by default). Sidekick is a conversational agent that helps investigators and analysts get work done without leaving the platform — navigating searches, summarising cases, building queries, and running analyses.

Sidekick uses an **agentic tool-calling pattern** via the `Anthropic.SDK` package: each user message is sent to Claude with a set of registered tools. Claude decides which tools to invoke, executes them, and streams back a natural-language response via Server-Sent Events.

**Configuration:**

| Setting | Default | Description |
|---|---|---|
| `Feature.Sidekick` | false | Enables the feature at the API level |
| `Sidekick.Model` | claude-sonnet-4-6 | Claude model to use |
| `Sidekick.MaxSessionMessages` | 10 | Messages retained before compaction |
| `Sidekick.MaxToolRounds` | 5 | Max tool execution rounds per request |
| `Sidekick.MaxRetries` | 3 | Retries on transient API errors (429, 529, 503) |
| `Sidekick.MaxTokens` | 16384 | Max output tokens per Claude response |
| `Sidekick.UseClientIdKeyVault` | false | Per-client API key in prod Key Vault |
| `Sidekick.SystemPrompt` | (default prompt) | Overridable system prompt |

**Sensitivity levels — controls which tools Claude can use:**

| Level | Capability | Tools |
|---|---|---|
| 0 (always on) | Basic product info, jokes, security reporting, page context | `GetAppInformation`, `TellJoke`, `ReportMaliciousPrompt`, `GetPageContext` |

## Secure · Modules (cont. 2)
_chunk 546 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

| 2+ | Search navigation, composer editing, running searches, result analysis | `ComposerEditor`, `GetSearch`, `GetQuicklink`, `RunSearch`, `GetDashboard`, `GetSourceApps`, `GetRepositoryData`, `GetReportDefinition`, `GetGeneratedReport`, `AnalyzeSearchResults` |
| 3+ | Work items, investigations, cases, consumer profiles | `GetWorkItems`, `GetAllCases`, `GetInvestigationData`, `SearchProfiles`, `GetProfile` |
| 4 | Full workflow: actions, transaction data, analysis, investigation actions | `GetAnalysisResult`, `GetWorkItemAbandonReasons`, `ActionWorkItem`, `GetWorkItemDetails`, `GetCaseDetails`, `ActionCase`, `GetInvestigationFacts`, `GetWorkItemEvents`, `GetTransactions`, `GetTransactionDetails`, `GetConsumerTransactions`, `GetInvestigationAbandonReasons`, `ActionInvestigation` |

**Key source locations:**

| Layer | Location |
|---|---|
| React UI | `Sources/UI/Components/src/_react/src/apps/sidekick/` |
| API controller | `Sources/UI/PlatformUI/Areas/Sidekick/Controllers/SidekickApiController.cs` |
| Service | `Sources/Core/Core/Sidekick/Services/SidekickService.cs` |
| Claude client | `Sources/Core/Core/Sidekick/Services/ClaudeClient.cs` |
| Tools | `Sources/Core/Core/Sidekick/Tools/` |
| DB stored procedures | `Sources/Databases/Platform/Programmability/Platform/sidekick/` |
| ControlPanel admin | `Sources/UI/ControlPanel/_react/src/apps/control-panel/pages/sidekick/` |

**Session & memory model:**
- Sessions are persisted to SQL Server (`sidekick.SessionInsert` / `sidekick.MessageInsert`)
- In-memory session store caches active sessions with a 30-minute TTL; on cache miss, sessions are rehydrated from the database
- When a session reaches `Sidekick.MaxSessionMessages`, Claude summarises the conversation into a placeholder and the window resets
- `ClaudeClient.CompactHistory()` strips tool-use roundtrips from old turns and drops complete old turns if still over the 150k-token budget
- Prompt caching enabled via `PromptCacheType.AutomaticToolsAndSystem`

**Local dev API key setup:**
```bash
dotnet user-secrets set "arp:local:000:sidekick:apikey" "YOUR_API_KEY"
```

[Sidekick wiki](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/477251502081/Sidekick)

### Metrics

Allows analysts to define and schedule KPI calculations. Metrics are stored over time, enabling trend analysis. Metrics also feed into AI Outliers.

### Reports and Dashboards

Scheduled reports can be emailed to users. Dashboards provide summary views per role. Store users typically see only their location's dashboard.

### Portals

Configurable landing pages per customer, often used to provide a summary view or quick access to key searches and reports.

## Secure · Permissions and data policies
_chunk 547 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

Access to data in Secure is controlled at three levels:

- **Role (Permission Group)** — What features you can access (e.g. Analyst can write searches, Store User cannot).
- **Location hierarchy** — What locations you can see data for. A district manager sees their district; a store manager sees their store.
- **Team** — Filters like "ORC Team" or "Digital Fraud Team" restrict what work items appear in a user's queue.

These three combine automatically based on the user's profile. There is no manual row-level filtering in queries — data policies are applied at the service layer.

[Permission Groups matrix](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474657783971/Secure+5+Permission+Groups+-+Application+Level)

## Secure · Feature flags
_chunk 548 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

Not every feature is on for every customer. Secure uses feature flags (config items in the database, seeded from arpfiles) to control which modules and behaviours are active per tenant. When working on a flagged feature, check whether it is enabled for Astromart locally.

Rule: always use **truthy** flags (`enableWidget = true`). Never use falsy flags like `disableWidget = false`.

[Feature Flags](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/1147866864/Feature+Flags)

## Secure · SSO
_chunk 549 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/secure.md_

Most enterprise customers use Single Sign-On. Secure supports SAML2 (99% of customers) and OpenID Connect. The customer's Identity Provider (IDP) sends claims to Secure at login. Secure trusts those claims to determine the user's identity, roles, teams, and location access. Appriss Retail has no access to the customer's IDP.

**SSO+** is a Secure-side tool that allows administrators to augment SSO claims when the customer's IDP cannot send full permission data.

[SSO documentation](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474863730689/SSO+-+Single+Sign+On+-+Start+here)

---

*Back: [Personas](../01-company/personas.md) · Next: [Platform Unification](platform-unification.md)*

## Snowflake · Overview
_chunk 550 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/snowflake.md_

Snowflake is the active analytics warehouse. It hosts the ARDM (raw POS and reference data) and a per-client Secure schema that sits alongside it. It is replacing the legacy Greenplum warehouse — see [Greenplum (legacy)](greenplum.md) for the outgoing system.

---

## Snowflake · Database and schemas
_chunk 551 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/snowflake.md_

Each environment has its own database, named:

```
ARP_{SLOT}
```

**Examples:** `ARP_PRODUCTION`, `ARP_STAGING`, `ARP_DEV`, `ARP_QA`, `ARP_CICD`, `ARP_SHOWCASE`.

Within each database there are two kinds of schema: ARDM schemas (raw transaction data) and per-client Secure schemas (Secure-owned data joined to ARDM at query time).

### ARDM schemas

Contain the raw transaction data, loaded by the SnowTime pipeline (DBT Core):

| Schema | Content |
|---|---|
| `ARDM_V1`, `ARDM_V2`, `ARDM_V3` | Versioned transaction schemas (columns differ by version). Each client's data lives in these shared schemas. |
| `ARDM_000` | Reference data shared across all clients (enumerations, calendar periods) |

For staging/production real clients (`ClientId >= 20`), the ARDM is in a separate database:

| Context | ARDM schema |
|---|---|
| Dev/test or `ClientId < 20` | `ARP_{SLOT}.ARDM_V{1|2|3}` and `ARP_{SLOT}.ARDM_000` |
| Staging / Production real clients on legacy GP-replicated path | `ARDMPROD.ARDM_{PaddedClientId}` and `ARDMPROD.ARDM_000` |
| Staging / Production real clients on SnowTime path | `{SnowflakeTargetArdmDatabase}.C{PaddedClientId}_{Abbreviation}` and `{SnowflakeTargetArdmDatabase}.ARDM_000` |

#### Target ARDM Database toggle (per-client, per-environment)

Real clients can run against either the GP-replicated `ARDMPROD` database or a SnowTime-produced Snowflake ARDM database. The toggle is the `SnowflakeTargetArdmDatabase` column on `arp.Clients` (Configuration DB; `nvarchar(50) NOT NULL DEFAULT 'ARDMPROD'`). Supported values today are `ARDMPROD`, `ARDM_STAGING`, `ARDM_PRODUCTION`; the column accepts any string so new SnowTime databases can be added without a schema change.

- **`ARDMPROD` (default for every existing row)** — legacy path. Per-client schema is `ARDMPROD.ARDM_{PaddedClientId}`; the SVC role is granted the blanket `ARDMPROD_RO` role (read across every client).
- **A SnowTime DB name** — SnowTime path. Per-client schema is `{db}.C{PaddedClientId}_{Abbreviation}`; the SVC role is granted only `{db}_C{PaddedClientId}_{Abbreviation}_RO`, scoped to that one client's schema (plus shared `{db}.ARDM_000` access bundled into the same role).

The arpfiles source for this column is the top-level `SnowflakeTargetArdmDatabase` field on the client's `arp_Clients[0]` entry in `seed-manifest.json` (base) or `seed-manifest.{env}.json` (per-environment override). `ClientContext.SnowflakeTargetArdmDatabase` reads via the two-layer `GetClientSeedValue<string>` lookup (env wins over base) — the same lookup used for `Abbreviation`, `DatabaseServerID`, and `ArdmVersion`. Test clients (`ClientId < 20`) and dev environments always use the mock `ARP_{SLOT}.ARDM_V{version}` path regardless of the column.

The column drives three places consistently: Lunar's `$(SnowflakeArdmSchemaName)` / `$(SnowflakeArdm000SchemaName)` substitutions, the per-client search path emitted by `CreateClientSchemaAndRoles.yaml`, and the grant script selected by that same pipeline (`GrantStgPrdArdmRoles.sql` for legacy, `GrantSnowtimeArdmRoles.sql` for SnowTime). The consolidated `ClientManifests/arp_Clients.{env}.json` artifact (produced by `Tools/PipelineUtilities/Actions/Build/ExtractMinimalClientManifests.cs`) also carries `SnowflakeTargetArdmDatabase` so deployment-time pipelines can read it without re-merging seed manifests.

To re-target an existing client at a different ARDM database, run the `{Region}{Slot}SetTargetArdmDatabase` pipeline under `Pipelines/Deployments/Databases/Snowflake/SetTargetArdmDatabase/`. It updates `SEARCH_PATH` on the SVC users, applies the appropriate ARDM grant for the new database, re-runs Lunar with `targetDatabases=snowflake` and `upgradeFlags=Function,View,Procedure` so programmability redeploys against the new ARDM without re-attempting EF migrations on the per-client Secure schema, and (when an explicit override was selected) uploads the modified `seed-manifest.{env}.json` to the ArpFiles blob so future Lunar runs keep substituting against the new ARDM. The pipeline `snowflakeTargetArdmDatabaseOverride` parameter is a dropdown of `use-arpfiles | ARDMPROD | ARDM_STAGING | ARDM_PRODUCTION`; pick `use-arpfiles` to read the value from the client manifest's `SnowflakeTargetArdmDatabase` field. **Operator follow-up:** raise an arpfiles git PR setting `SnowflakeTargetArdmDatabase` on the `arp_Clients[0]` entry of the client's `seed-manifest.{env}.json` so a future arpfiles redeploy from git doesn't wipe the blob change.

## Snowflake · Database and schemas (cont. 2)
_chunk 552 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/snowflake.md_

### Per-client Secure schemas

Secure-owned data that sits alongside ARDM and is joined with it at query time. There are two per-client schemas:

| Schema | Naming | Purpose |
|---|---|---|
| Secure | `ARP_{SLOT}.C{PaddedClientId}_{Abbreviation}` | The main Secure-side schema — enumerations, user hierarchy assignments, user data, metrics, investigation→txn links |
| Platform mirror (WIP) | `ARP_{SLOT}.C{PaddedClientId}_{Abbreviation}_PLATFORM` | Replicated data from the MSSQL Platform DB for this client. Lets searches join Platform-DB tables in Snowflake without crossing engines |

**Examples:** `ARP_PRODUCTION.C001_AMT`, `ARP_PRODUCTION.C001_AMT_PLATFORM`

The Snowflake search path for each client includes both per-client schemas and the relevant ARDM schemas, so queries can reference everything transparently.

---

## Snowflake · Per-Client Secure Schemas
_chunk 553 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/snowflake.md_

Naming and search-path detail are above under [Per-client Secure schemas](#per-client-secure-schemas). This section covers what each schema holds and why they exist.

**These are *not* the same as the `secure` schema inside the SQL MI platform database** — see [SQL MI](sql-mi.md#per-tenant-platform-database-schemas) for that one.

### Main Secure schema

Holds Secure-owned data that needs to be joinable with ARDM transactions:

- **Enumeration / reference data** — display values for enumerated fields such as transaction types (1→Sale, 2→Return, etc.)
- **User location-hierarchy assignments** — which stores/districts/regions a user is scoped to
- **User data** — user-uploaded CSV files materialised to rows containing JSON representations of each CSV row. Queried using Snowflake JSON support.
- **Metric definitions** — the definitions used by metric generation
- **Generated metrics** — the outputs of metric calculations run against ARDM data
- **Transaction IDs referenced by investigations** — the link between an investigation in `factboard` (on SQL MI) and the underlying ARDM transactions

### Platform DB mirror (WIP)

Holds tables replicated from the MSSQL Platform database for this client. Currently in progress. Once populated, searches that previously had to cross engines (Snowflake ARDM ↔ SQL MI Platform) can run as a single Snowflake query joining ARDM rows directly to mirrored Platform tables.

### Why these schemas exist

Secure searches run on the analytics warehouse, not on SQL MI. Anything a user-authored search needs to join against ARDM rows must also live in the warehouse — otherwise the join would have to cross database engines. The main schema covers Secure-owned data; the `_PLATFORM` schema (WIP) extends the same idea to MSSQL Platform-DB content.

Expect to see joins like:

```sql
select ...
from ARDMPROD.ARDM_001.ardm_header H
join ARP_PRODUCTION.C001_AMT.secure_enumerationreferencedata R on ...
join ARP_PRODUCTION.C001_AMT.secure_locationhierarchyuserassignments LHUA on ...
-- once the _PLATFORM mirror is populated:
join ARP_PRODUCTION.C001_AMT_PLATFORM.<mirrored_table> P on ...
```

---

## Snowflake · Provisioning
_chunk 554 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/snowflake.md_

New client schemas are created via the `CreateClientSchemaAndRoles` pipeline (`Pipelines/Deployments/Databases/Snowflake/`). This creates the client schema, RSA key pair, and grants roles for ARDM access.

See [Database Deployment Pipelines](../../../Pipelines/docs/database-deployments.md) for the full pipeline reference.

Schema-level changes to the Secure side are managed by the `Sources/Databases/Snowflake/` EF project. See [Lunar](lunar.md) for the installer and [EF Core Migrations](lunar.md#ef-core-migrations) for the workflow.

---

## Snowflake · Connecting to Snowflake
_chunk 555 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/snowflake.md_

We have two Snowflake accounts, one per region:

| Region | Account | Hostname |
|---|---|---|
| US | `OKB13541-JN80103` | `OKB13541-JN80103.snowflakecomputing.com` |
| EU | `OKB13541-NEUAZ` | `OKB13541-NEUAZ.snowflakecomputing.com` |

Authenticate via AzureAD. For local development the EU account (`NEUAZ`) is recommended.

### Web app

1. First time: go to <https://myapplications.microsoft.com/> and pick **Snowflake EU** or **Snowflake US**.
2. After that, <https://app.snowflake.com/> — then choose **JN80103** (US) or **NEUAZ** (EU).

### Running Lunar / Secure against Snowflake locally

Secure and Lunar use the [`Snowflake.Data`](https://github.com/snowflakedb/snowflake-connector-net) .NET library. Connection strings contain `$KV()` references for secret values — locally these resolve from [dotnet user-secrets](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets?view=aspnetcore-8.0&tabs=windows), in real environments they resolve from Azure Key Vault.

**1. Set your user's search path** (once, from the Snowflake web app worksheet):

```sql
USE DATABASE ARP_DEV;
ALTER USER SET SEARCH_PATH = 'C001_AMT, ARDM_V2, ARDM_000, PUBLIC';
```

**2. Generate a PAT token** from the web app under **Settings → Authentication**. Save the value in your 1Password Employee Vault for future reference.

**3. Save the PAT locally as user-secrets.** From `Sources/Databases/Installer/Installer`:

```bash
cd ~/Secure/Sources/Databases/Installer/Installer
dotnet user-secrets set "arp:local:000:snowflake:user" "YOUR-EMAIL@trebu.co"
dotnet user-secrets set "arp:local:000:snowflake:token" "YOUR PAT TOKEN"
```

**4. For Lunar deploys against `ARP_DEV`**, add a Snowflake connection string to the client's `database-manifest.local.json` in arpfiles:

```json
"snowflake": {
  "connectionString": "account=OKB13541-$(SnowflakeAccountName);user=$KV(arp:local:000:snowflake:user);authenticator=programmatic_access_token;db=ARP_DEV;schema=C$(PaddedClientId)_$(ClientAbbreviation);role=SVC_ARP_DEV_$(PaddedClientId)_$(ClientAbbreviation)_LUNAR_ROLE;warehouse=SECURE_XS_WH;client_store_temporary_credential=true;TOKEN=$KV(arp:local:000:snowflake:token)"
}
```

Then update `CLIENTIDS` in the database solution's `launchSettings.json` with the target client ID and run Lunar as normal.

**Note:** receipts won't work until the Data API is enabled and configured — Snowflake has no `ardm_json` equivalent.

### Connecting from Rider / DataGrip

Preferred method is PAT auth (avoids repeated login prompts):

| Field | Value |
|---|---|
| Data source | Snowflake |
| Host | `OKB13541-JN80103.snowflakecomputing.com` (US) or `OKB13541-NEUAZ.snowflakecomputing.com` (EU) |
| Authentication | Username & Password |
| User | Your `@trebu.co` email address |
| Password | Your PAT token |

**Fallback — external browser auth** (useful if you can't generate a PAT, e.g. during a Snowflake outage):

| Field | Value |
|---|---|
| Authentication | Authenticator |
| Authenticator | `EXTERNALBROWSER` |
| User | Your `@trebu.co` email address |

For screenshots of each step, see the source Confluence page: [Connecting to Snowflake](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475916271617/Connecting+to+Snowflake).

---

*Back: [Database Architecture](../databases.md)*

## SQL Managed Instance · Overview
_chunk 556 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/sql-mi.md_

The platform's operational state lives on Azure SQL Managed Instance (SQL MI). Each environment/region/slot has one or more SQL MIs hosting:

- A single shared **configuration database** that bootstraps the platform
- A pair of **platform + reference** databases per tenant

For analytics data (POS, returns, employees), see [Snowflake](snowflake.md) and [Greenplum (legacy)](greenplum.md).

---

## SQL Managed Instance · Naming Conventions
_chunk 557 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/sql-mi.md_

### SQL Managed Instance (server)

```
sqlmi-{env}-{region}-arp-{serverId}-{slot}
```

| Placeholder | Example values |
|---|---|
| `{env}` | `dev`, `qa`, `stg`, `prd` |
| `{region}` | `wus2`, `neu` |
| `{serverId}` | Zero-padded 3 digits: `001`, `002`, `003` (clients are distributed across multiple MIs) |
| `{slot}` | `dev`, `cicd`, `showcase`, `qa`, `staging`, `production` |

**Example:** `sqlmi-prd-wus2-arp-001-production`

### Shared configuration database

```
sqldb-{env}-{region}-arp-{slot}-configuration
```

**Example:** `sqldb-prd-wus2-arp-production-configuration`

Only one per environment/region/slot. The platform bootstraps off this database to find everything else. Credentials are held in Azure Key Vault under `{slot}.{region}.GlobalConfiguration.Username` / `.Password` / `.ServerID`.

### Per-tenant platform and reference databases

Each client has **two** databases on the MI:

```
sqldb-{env}-{region}-arp-{slot}-{paddedClientId}-{abbreviation}-platform
sqldb-{env}-{region}-arp-{slot}-{paddedClientId}-{abbreviation}-reference
```

**Examples:**
- `sqldb-prd-wus2-arp-production-001-astromart-platform`
- `sqldb-prd-wus2-arp-production-001-astromart-reference`

`platform` is the working database (schemas described below). `reference` holds slower-moving reference data.

---

## SQL Managed Instance · The Shared Configuration Database
_chunk 558 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/sql-mi.md_

The configuration database is the glue that connects the platform to its tenants. It contains:

| What | Purpose |
|---|---|
| **Connection strings** | How the application locates each tenant's platform and reference databases at runtime |
| **Client metadata** | Tenant identity, abbreviations, display names, environment-specific settings |
| **Feature flags and module enablement** | Per-client toggles that control which platform modules are active |

It uses two schemas:

- `arp` — clients, connection strings, configuration items, logs
- `secure` — general security-related configuration

See [Multi-Tenancy and Connection String Resolution](../databases.md#multi-tenancy-and-connection-string-resolution) for how the platform uses this database at runtime.

### Client attributes table

Of particular interest for analytics and cross-team work is the **client attributes** table. It stores per-client flags for:

- Enabled modules (e.g. SecureGPT, Sidekick, eCom, Engage)
- ARDM version per client (V1, V2, V3)
- Other operational metadata (e.g. `Store` — whether the client sends store/POS data; `Engage` — whether they use the Engage module)

This table is primarily operational (the application reads it to decide what features to show), but it is useful context when you need to understand which clients have access to which capabilities. The Snowflake client-schema pipeline also reads these attributes to decide which ARDM / Engage role grants to apply.

---

## SQL Managed Instance · Per-Tenant Platform Database Schemas
_chunk 559 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/sql-mi.md_

The per-client `platform` database is where the application keeps its operational state. It is organised into many schemas, each owning a distinct concern:

| Schema        | Contents                                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| `secure`      | The **repo** table (a virtual file system used by the app), plus general Secure tables                             |
| `factboard`   | Investigations created in the app (Investigations were previously called Factboards)                               |
| `workview`    | Generated work items (flagged search results queued to investigators) and work item generation history             |
| `fti`         | Additional tables used in work items (legacy name "Fast-Track Investigations") — which transactions they identified |
| `membership`  | Users, teams, groups, and permissions                                                                              |
| `incident`    | Tables used by the Incident app                                                                                    |
| `sso`         | SSO configuration                                                                                                  |
| `cctv`        | CCTV integration                                                                                                   |
| `job`         | Deprecated — previously used by the "Job System", HATR's predecessor                                               |

The schema list is large because the platform has grown over many years. Some schemas back active modules, some are deprecated but retained for historical customer data. When exploring a tenant database for the first time, focus on `secure`, `workview`, `factboard`, and `membership` — these cover the most commonly-touched functionality.

Note: the `secure` schema inside the platform database is *not* the same thing as the per-client Secure schema in the analytics warehouse. See [Snowflake — Per-Client Secure Schema](snowflake.md#per-client-secure-schema).

---

## SQL Managed Instance · Schema management
_chunk 560 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/sql-mi.md_

Schema changes to platform and configuration databases are tracked via EF Core migrations; stored procedures and functions live in `Programmability/`. See [Lunar](lunar.md) for the installer and [EF Core Migrations](lunar.md#ef-core-migrations) for the workflow.

---

*Back: [Database Architecture](../databases.md)*

## Secure Platform — React UI Style Guide · Overview
_chunk 561 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

This guide covers the conventions and components you need to build a new screen in this codebase. Follow it so new screens look and behave consistently with existing ones.

All shared components live in `Sources/UI/Components/src/_react/src/shared/components/`.
Import them using the `@shared` alias: `import { Section } from '@shared/components/section/section.component'`.

---

## Secure Platform — React UI Style Guide · 1. Quick Start — Anatomy of a New Page
_chunk 562 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

**Use `PageLayout` for new pages.** It wraps the shell header (breadcrumbs, title, toolbar) and automatically manages portals.

```jsx
import React from 'react';
import { PageLayout } from '@shared/components/page-layout/page-layout.component';
import { Section } from '@shared/components/section/section.component';
import { MyConstants } from './constants';

export function MyPage() {
    return (
        <PageLayout
            breadcrumbs={[
                { title: Constants.Home, link: '/home', external: false },
                // Add parent breadcrumb(s) as needed — e.g. Admin, Reports, Cases, etc.
                { title: Constants.ParentTitle, link: '/parent', external: false },
                // Omit the current page for list screens; include for detail/edit screens
                { title: Constants.PageTitle, link: '/parent/current', external: false }
            ]}
            title={Constants.PageTitle}
            documentTitle={Constants.PageTitle}
            toolbar={
                <ul className='flex-toolbar'>
                    <li className='nav-item'>
                        <button type='button' className='nav-link' onClick={handleAction}>
                            <span className='fa fa-fw fa-plus mr-2' aria-hidden={true} />
                            {Constants.New}
                        </button>
                    </li>
                    {/* Add more toolbar items as needed */}
                </ul>
            }
        >
            {/* Page body — Sections, ParameterBox, grids, etc. */}
            <Section title={Constants.SectionTitle}>
                { /* content */ }
            </Section>
        </PageLayout>
    );
}
```

**Rules:**
- `PageLayout` is the standard wrapper for list and detail screens — use it instead of manual portals.
- Pass `breadcrumbs`, `title`, `documentTitle`, and `toolbar` as props.
- `toolbar` expects `<ul className='flex-toolbar'>` with each action in `<li className='nav-item'>`.
- Children of `PageLayout` are the page body — usually `Section` components.
- Every page must set `documentTitle` so the browser tab title updates on navigation.
- **Do not use `setPageTitle`** — it's a workaround for stale component state. `PageLayout` handles title management automatically. See `src/apps/incident/pages/admin-locations/list.component.js` for correct usage.

### Legacy pattern (manual portals)

For pages that cannot use `PageLayout`, you can still manage portals individually:

```jsx
import React from 'react';
import { Toolbar } from '@shared/components/toolbar/toolbar.component';
import { PageTitle } from '@shared/components/page-title/page-title.component';
import { Compass } from '@shared/components/compass/compass.component';
import { CompassLinks } from '@shared/components/compass-links/compass-links.component';
import { Section } from '@shared/components/section/section.component';

export function MyPage() {
    return (
        <div className='page-content tw:flex tw:flex-col'>

            {/* Left toolbar — filter controls, primary actions */}
            <Toolbar>
                <ul className='flex-toolbar'>
                    <li className='nav-item'>{ /* each button or control */ }</li>
                </ul>
            </Toolbar>

            {/* Breadcrumbs — mirrors the route hierarchy */}
            <Compass>
                <CompassLinks links={[
                    { title: 'Incident', link: '/home', external: false },
                    { title: 'Admin', link: '/admin', external: false },
                    { title: 'Feature Name', link: '/admin/feature', external: false }
                ]} />
            </Compass>

            {/* Page title — renders into the shell header via a portal */}
            <PageTitle documentTitle='My Page'>My Page</PageTitle>

            {/* Page body — one or more Sections */}
            <Section title='Section Title'>
                { /* content */ }
            </Section>

        </div>
    );
}
```

**Legacy rules:**
- The root element is `<div className='page-content'>`.
- `Toolbar`, `PageTitle`, and `Compass` use React portals — declare them inside your component even though they render elsewhere.
- Use this pattern only for pages with custom header layouts that `PageLayout` doesn't support.

### Breadcrumb rules (`Compass` / `CompassLinks`)

## Secure Platform — React UI Style Guide · 1. Quick Start — Anatomy of a New Page (cont. 2)
_chunk 563 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

Breadcrumbs must mirror the route hierarchy — **ancestor entries only, not the current page**. The current page name is shown in the `<PageTitle>` and `<title>` element; it must not appear in the breadcrumb trail.

| Screen depth | Breadcrumb trail |
|---|---|
| App root (e.g. Admin tile list) | `Incident` |
| Feature list (e.g. Manage Smart Alerts) | `Incident` → `Admin` |
| Feature detail/edit | `Incident` → `Admin` → `Manage Smart Alerts` |

All entries in the breadcrumb trail are clickable links (`link` property required on every item). The current page is never included.

Use `IncidentConstants` for all labels — never inline strings. Set `external: false` on all internal routes.

---

## Secure Platform — React UI Style Guide · 2. Colors
_chunk 564 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

All colors are defined as CSS custom properties in `theme.css`. **Never use hardcoded hex values** — always use a token.

### Brand & structural tokens

| Token | Light value | Use for |
|---|---|---|
| `--primary-base` | `#5BC8D9` | Primary buttons, active states, links |
| `--primary-dark` | `#247683` | Primary hover states |
| `--primary-light` | `#7CDDEC` | Subtle accent backgrounds |
| `--secure-primary-text` | `#1D3E6F` | All body text, headings, button labels |
| `--default-text` | `#212529` | General paragraph text |
| `--muted` | `#627895` | Placeholder text, secondary labels |
| `--text-disabled` | `#BAC6D6` | Disabled input text |
| `--background` | `#E7ECF4` | Page background |
| `--section-background` | `#FFFFFF` | Card/section backgrounds |
| `--section-border` | `#DEE3E8` | Card borders |
| `--border-strong` | `#BAC6D6` | Prominent dividers |

### Semantic tokens

Use these for status, alerts, and validation — not for decoration.

| Token | Use for |
|---|---|
| `--success-secure` | Success text, icons |
| `--success-button` / `--success-button-hover` | Success action buttons |
| `--success-alert-box` | Alert box background (success) |
| `--warning-secure` | Warning text, icons |
| `--warning-button` / `--warning-button-hover` | Warning/caution buttons |
| `--warning-alert-box` | Alert box background (warning) |
| `--danger-secure` | Destructive action text, icons |
| `--danger-button` / `--danger-button-hover` | Destructive action buttons |
| `--danger-alert-box` | Alert box background (danger) |
| `--info-secure` | Informational text, icons |
| `--info-alert-box` | Alert box background (info) |

### Dark mode

Dark mode is triggered by the `.dark-theme` class on `<html>`. Every token above has a dark override already defined in `theme.css`. If you define a new CSS variable, add both a light and dark value. Never use the `--dark-gray-*` palette directly in component styles — use the structural tokens (`--background`, `--section-background`, etc.) which automatically switch.

### Shadows

| Token | Use for |
|---|---|
| `--shadow-small` | Dropdowns, small popovers |
| `--shadow-medium` | Cards, sections |
| `--shadow-large` | Modals, lightboxes |

---

## Secure Platform — React UI Style Guide · 3. Typography
_chunk 565 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

The platform does not use a custom font stack — it inherits Bootstrap's system-font stack. Follow these rules:

- **Headings:** many shared components (`Section`, `PageLayout`, `Parameter`, etc.) already have `title` props — use those instead of writing custom `<h1>`–`<h6>` tags. This keeps styling consistent across the app.
- **Body text:** `color: var(--default-text)`, default Bootstrap font size (1rem / 16px).
- **Muted / secondary text:** `color: var(--muted)`.
- **Small labels:** Bootstrap `.small` class or `font-size: 0.875rem`.
- **Do not** set `font-size` in pixels on individual elements — use Bootstrap scale or rem.

---

## Secure Platform — React UI Style Guide · 4. Spacing
_chunk 566 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

Use **Bootstrap utility classes only**. Do not write raw `px` or `rem` values in component-scoped CSS for spacing.

Bootstrap's scale uses 0.25rem (4px) increments:

| Class | Value |
|---|---|
| `p-1` / `m-1` | 4px |
| `p-2` / `m-2` | 8px |
| `p-3` / `m-3` | 16px |
| `p-4` / `m-4` | 24px |
| `p-5` / `m-5` | 48px |

**Standard page spacing:**
- Between top-level Sections: `mb-3` on each Section wrapper div.
- Inside a Section, between form fields: `mb-3`.
- Between action buttons: `ml-2` on all buttons after the first.
- Toolbar controls: spacing is handled automatically by the `gap` on `.flex-toolbar` — do not add `mr-2` between toolbar items.

Pixel values are only acceptable in component-scoped CSS for structural layout (e.g. a fixed-width sidebar, a sticky header `top` offset). Even then, prefer multiples of 4.

---

## Secure Platform — React UI Style Guide · 5. Layout
_chunk 567 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

### Page grid

Use Bootstrap's 12-column grid inside sections. Common patterns:

```jsx
{/* Two-column form layout */}
<div className='row'>
    <div className='col-md-6'>{ /* left column */ }</div>
    <div className='col-md-6'>{ /* right column */ }</div>
</div>

{/* Three-column info tile row */}
<div className='row'>
    <div className='col-md-4'>{ /* tile */ }</div>
    <div className='col-md-4'>{ /* tile */ }</div>
    <div className='col-md-4'>{ /* tile */ }</div>
</div>

{/* Full-width content (data grid, etc.) */}
<div className='row'>
    <div className='col-12'>{ /* full width */ }</div>
</div>
```

### Section component

`Section` is the standard content container. Always use it instead of raw `<div>` wrappers with custom borders.

```jsx
{/* Basic section */}
<Section title='My Section'>
    { /* content */ }
</Section>

{/* Collapsible section (starts collapsed by default) */}
<Section title='Filters' collapsible collapsed={true}>
    { /* content */ }
</Section>

{/* Section with an action button in the header */}
<Section
    title='Results'
    adornment={<button className='btn btn-primary'>Export</button>}
>
    { /* content */ }
</Section>

{/* Section with AI icon in header */}
<Section title='AI Analysis' displayAiIcon={true}>
    { /* content */ }
</Section>
```

**Section props:**

| Prop | Type | Default | Purpose |
|---|---|---|---|
| `title` | string | — | Section heading text |
| `collapsible` | bool | `false` | Adds expand/collapse toggle |
| `collapsed` | bool | `true` | Initial collapsed state |
| `adornment` | element | — | Renders top-right of the section header (use for action buttons) |
| `displayAiIcon` | bool | — | Shows the AI sidebar icon next to the title |
| `additionalClass` | string | `''` | Extra CSS class on the root div |

### Section headers and sub-headers

Always pass a `title` to `<Section>` — never use a raw `<div>` as a section heading. The `title` prop renders the standard platform header (1.25 rem bold, rounded top, correct background).

```jsx
{/* Correct */}
<Section title='Alert Configuration'>...</Section>

{/* Wrong — raw div bypasses the platform header style */}
<div className='fw-bold'>Alert Configuration</div>
```

When a section contains two logical panels side by side and you need a heading for each panel, use this style so the panel labels visually match the Section header weight and color:

```jsx
<div style={{ fontSize: '1.1rem', fontWeight: 'bold', color: 'var(--secure-primary-text)', marginBottom: '0.75rem' }}>
    Panel Label
</div>
```

Use `var(--secure-primary-text)` (dark navy). **Never use `var(--default-text)` (gray) for headings** — it reads as secondary/muted content, not a label.

**When `Section` is not needed:** if your page contains only a `LocalDataDataGrid` (optionally with a `ParameterBox` filter bar above it), do not wrap the grid in a `<Section>`. The grid's built-in title and header are sufficient. Use `Section` only when you have additional form fields, content panels, or multiple logical sections on the page.

---

### Multi-tab detail pages

When a detail/edit screen has more than one logical group of fields, use the **sidebar nav + child routes** pattern. This is the standard for all admin detail screens in the Incident app.

**Visual structure:**

```
┌─ Toolbar (Save) ──────────────────────────────────┐
├─ Compass (breadcrumbs) ───────────────────────────┤
├─ Sidebar ──────┬─ Content area ───────────────────┤
│  Alert Config  │  <Section title='Alert Config'>  │
│  Email Recip.  │    <div className='row'>         │
│  Build Filters │      <div className='col-md-6'>  │
│                │        fields…                   │
│                │      </div>                      │
│                │    </div>                        │
│                │  </Section>                      │
└────────────────┴──────────────────────────────────┘
```

**Sidebar tabs use `NavLink`** (from `react-router-dom`), not `<button>` or `<a role="button">`. `NavLink` renders a real `<a>` element, which picks up the platform's `.sidebar li a` CSS automatically for hover, active, and padding.

```jsx
<Sidebar hideHeader={true}>
    <ul>
        <li>
            <NavLink id='tab-first' to={basePath} end>
                {MyConstants.TabFirst}
            </NavLink>
        </li>
        <li className='mt-1'>
            <NavLink id='tab-second' to={`${basePath}/second`}>
                {MyConstants.TabSecond}
            </NavLink>
        </li>

## Secure Platform — React UI Style Guide · 5. Layout (cont. 2)
_chunk 568 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

    </ul>
</Sidebar>
```

The `end` prop on the first tab prevents it matching as active on all child routes.

**Content is rendered by `<Outlet>`**, not by `activeTab` state or conditional JSX. Each tab is a separate route that renders a separate section component. The shell component owns shared form state and passes it down via `<Outlet context={...}>`.

```jsx
{/* Shell — owns form state, renders sidebar and outlet */}
<Outlet context={{ form, setField, recordId, isNew }} />
```

```jsx
{/* Section component — reads context, renders its own fields */}
export function FirstTab() {
    const { form, setField } = useOutletContext();
    return (
        <div className='content-area'>
            <Section title={MyConstants.TabFirst}>
                ...
            </Section>
        </div>
    );
}
```

**Do not use `activeTab` state + conditional JSX** to switch between tab content. That approach breaks browser history, prevents deep-linking, and makes the active tab style fight against NavLink's built-in active class.

**Reference implementation:** `src/apps/incident/pages/admin-smart-alerts/` — shell in `detail.component.js`, sections in `sections/`.

**Routing setup for add/edit screens:** When both `/new` and `/:id` routes use the same detail component with the same child sections, define the child routes in a variable in `index.js` and reuse it. See `src/apps/incident/index.js` — `employeeDetailChildren` and `locationDetailChildren` are defined once, then passed to both the new and detail route configurations. This keeps the route structure DRY and ensures add and edit screens always show the same tabs.

---

### Flexbox patterns

For horizontal rows of items that don't need the full Bootstrap grid:

```jsx
{/* Space items apart */}
<div className='d-flex justify-content-between align-items-center'>
    <span>Label</span>
    <button className='btn btn-primary'>Action</button>
</div>

{/* Cluster items to the left */}
<div className='d-flex align-items-center'>
    <span className='mr-2'>Item 1</span>
    <span>Item 2</span>
</div>
```

---

## Secure Platform — React UI Style Guide · 6. Icons
_chunk 569 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

Use the `fa fa-fw fa-<name>` class pattern with a self-closing `<span>`. Never use `<i>`, never use `fa-solid`.

```jsx
{/* Correct */}
<span className='fa fa-fw fa-filter' />

{/* Incorrect — wrong element */}
<i className='fa-solid fa-filter'></i>

{/* Incorrect — missing fa-fw */}
<span className='fa fa-filter' />
```

`fa-fw` (fixed-width) ensures icons align consistently in lists and buttons without needing an inline `style` for width.

### Common icon-to-concept map

| Concept | Class |
|---|---|
| Add / create | `fa-plus` |
| Edit | `fa-pen` |
| Delete / remove | `fa-trash` |
| Save | `fa-floppy-disk` |
| Search / filter | `fa-magnifying-glass` |
| Filter (funnel) | `fa-filter` |
| Sort | `fa-sort` |
| Export / download | `fa-download` |
| Upload | `fa-upload` |
| External link | `fa-arrow-up-right-from-square` |
| View / eye | `fa-eye` |
| Hide | `fa-eye-slash` |
| Close / dismiss | `fa-xmark` |
| Expand (right) | `fa-chevron-right` |
| Collapse (down) | `fa-chevron-down` |
| Back (left) | `fa-chevron-left` |
| Warning | `fa-triangle-exclamation` |
| Info | `fa-circle-info` |
| Success / check | `fa-circle-check` |
| Error | `fa-circle-xmark` |
| Calendar | `fa-calendar` |
| Lock | `fa-lock` |
| User | `fa-user` |
| Loading (spinner) | `fa-spinner fa-spin` |
| Copy | `fa-copy` |
| Settings | `fa-gear` |
| Refresh | `fa-rotate` |

Use as: `<span className='fa fa-fw fa-<name>' />`

### Icon sizing

Use FA size modifiers when needed: `fa-sm`, `fa-lg`, `fa-xl`, `fa-2x`. Default (no modifier) matches the surrounding text size — this is correct for icons in buttons and labels.

---

## Secure Platform — React UI Style Guide · 7. Buttons
_chunk 570 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

### Decision tree — which button to use

```
Is this a TOOLBAR button (New / Edit / Delete / etc.)?
  YES → Does it need a distinct visual style (e.g. primary Add button)?
          YES → <button className='btn btn-primary'>
                 <span className='fa fa-fw fa-icon mr-2' aria-hidden={true}></span>{Label}
               </button>
          NO  → <button className='btn'>
                 <span className='fa fa-fw fa-icon mr-2' aria-hidden={true}></span>{Label}
               </button>

Is this an async operation (saves, submits, API calls)?
  YES → MotionButton
  NO  → Is this a destructive action (delete, remove)?
          YES → <button className='btn btn-danger'>
                 <span className='fa fa-fw fa-icon mr-2' aria-hidden={true}></span>{Label}
               </button>
          NO  → Is this the primary action on the screen?
                  YES → <button className='btn btn-primary'>
                         <span className='fa fa-fw fa-icon mr-2' aria-hidden={true}></span>{Label}
                       </button>
                  NO  → <button className='btn btn-secondary'>
                         <span className='fa fa-fw fa-icon mr-2' aria-hidden={true}></span>{Label}
                       </button>
```

**Toolbar button styling:** All button elements (including other elements styled as buttons with 'btn' className) must be inline so buttons remain adjacent with no vertical stacking. Always include an icon with `mr-2` spacing and `aria-hidden={true}` before the label: `<span className='fa fa-fw fa-icon mr-2' aria-hidden={true}></span>{label}`.

### Button type attribute

Always use `type='button'` on all `<button>` elements. A `<button>` inside a `<form>` defaults to `type='submit'`, which causes unexpected form submissions and page reloads.

```jsx
{/* Correct */}
<button type='button' id='add-item' onClick={handleAdd}>Add</button>

{/* Shared components handle this internally — only applies to raw <button> */}
<MotionButton ... />
```

### MotionButton (primary choice for form submissions)

Use `MotionButton` for any button that triggers a network request. It handles loading, success, and error states automatically with animated transitions.

```jsx
import MotionButton from '@shared/components/motion-button/motion-button.component';

<MotionButton
    idleLabel='Save'
    processingLabel='Saving...'
    successLabel='Saved'
    errorLabel='Failed'
    icon='fa-floppy-disk'    // optional — icon name (without fa- prefix is also accepted)
    showSuccess={this.state.saved}
    showError={this.state.error}
    loading={this.state.loading}
    isValid={this.state.formIsValid}   // turns button warning-colored when false
    processClick={() => this.save()}
    runOnEnter={true}                  // submits on Enter key
/>
```

**MotionButton props:**

| Prop | Type | Required | Notes |
|---|---|---|---|
| `idleLabel` | string | — | Default button label |
| `processingLabel` | string | — | Label while loading |
| `successLabel` | string | — | Label on success |
| `errorLabel` | string | — | Label on error |
| `icon` | string | — | Icon name (e.g. `'fa-check'`) |
| `svgIcon` | element | — | SVG element — alternative to `icon` |
| `showSuccess` | bool | yes | Drive from component state |
| `showError` | bool | — | Drive from component state |
| `loading` | bool | — | Drive from component state |
| `isValid` | bool | — | Defaults `true`. Set to validation result |
| `processClick` | func | yes | Called on click or Enter |
| `runOnEnter` | bool | — | Binds Enter key globally while mounted |
| `btnLg` | bool | — | Applies `btn-lg` Bootstrap size |
| `overrideClass` | string | — | Replaces the default `ml-auto` class |
| `disabled` | bool | — | Hard-disables regardless of state |

### Plain Bootstrap buttons

For navigation or non-async actions:

```jsx
{/* Primary action */}
<button className='btn btn-primary'>View Details</button>

{/* Secondary action */}
<button className='btn'>Other Action</button>

{/* Destructive */}
<button className='btn btn-danger'>Delete</button>

{/* Small variant — use inside Section adornments, toolbars */}
<button className='btn btn-primary'>Export</button>

{/* Icon + text — always icon on the left */}
<button className='btn btn-primary'>
    <span className='fa fa-fw fa-plus' />
    Add Item
</button>

{/* Link-style button — for inline text actions */}
<button className='btn btn-link'>Learn more</button>
```

### Toolbar button labels

## Secure Platform — React UI Style Guide · 7. Buttons (cont. 2)
_chunk 571 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

Use short, generic labels — never append the feature name to a button. The icon already communicates the action; the label just needs one word.

| Action | Label | Icon | Example |
|---|---|---|---|
| Create new record | `New` | `fa-plus` | `<span className='fa fa-fw fa-plus mr-2' aria-hidden={true}></span>New` |
| Create/add item | `Add` | `fa-plus` | `<span className='fa fa-fw fa-plus mr-2' aria-hidden={true}></span>Add` |
| Open selected record | `Edit` | `fa-edit` | `<span className='fa fa-fw fa-edit mr-2' aria-hidden={true}></span>Edit` |
| Remove selected record | `Delete` | `fa-trash` | `<span className='fa fa-fw fa-trash mr-2' aria-hidden={true}></span>Delete` |
| Save/submit changes | `Save` | `fa-save` | `<span className='fa fa-fw fa-save mr-2' aria-hidden={true}></span>Save` |
| Share/export | `Share` | `fa-share` | `<span className='fa fa-fw fa-share mr-2' aria-hidden={true}></span>Share` |
| Download/export data | `Export` | `fa-download` | `<span className='fa fa-fw fa-download mr-2' aria-hidden={true}></span>Export` |

Never use labels like "New Investigation", "Add Field", "Save Changes" — strip the context and use the action verb only. The icon + context of the page make the meaning clear.

### Non-lightbox button label word rules

These words have canonical replacements and must be used consistently:

| Avoid | Use instead | Notes |
|---|---|---|
| `Add` | `New` | Creating a new top-level record or item — "New Field", not "Add Field" |
| `Remove` | `Delete` | Destructive removal — "Delete Field", not "Remove Field" |
| `Update` | `Save` | Submitting a form change — never "Update" on a button |

**Lightbox buttons** must use `Save`, never `Add` or `Update`. The lightbox confirm action is always a save regardless of whether the underlying operation is a create or an edit.

Some `Add` and `Remove` instances were intentionally left unchanged where the context specifically means appending to or removing from a list (e.g. "Add" or "Remove" inside a condition builder row). If you are unsure, default to `New` / `Delete`.

> **No Refresh button.** Never add a Refresh button to list screens. Data is fetched on mount; after write operations (delete, save) the component re-fetches automatically by incrementing the grid key or invalidating the query. A manual refresh button is redundant and clutters the toolbar.

### Toolbar button placement rules

- **All primary and secondary actions** (Save, Delete, etc.) belong in the `<Toolbar>` component — this applies to both list screens and detail/edit screens.
- **Never** put action buttons at the bottom of a form or section. The toolbar is the single, consistent place users look for actions.
- **Never** add a Cancel or back button to the toolbar. Navigation back is handled via breadcrumbs (the `<Compass>` component).
- **Toolbar action order** (left to right): New · Edit · Delete · [other destructive actions].
- **Section-level actions** (e.g. "Export"): in the `adornment` prop of `<Section>`, right-aligned.
- **Never** put a primary action at both the top and bottom of the same screen.

### Disabled button appearance

Use the `disabled` attribute on any button element. Bootstrap handles disabled state styling automatically — reduced opacity, `pointer-events: none`, and muted colour.

```jsx
{/* Automatically styled as disabled when no row is selected */}
<button className='btn' disabled={selectedRecords.length !== 1} onClick={handleEdit}>
    <span className='fa fa-fw fa-pen mr-2' aria-hidden={true} />
    Edit
</button>
```

No custom CSS override is needed.

### Dividers in button rows

Use `<span className='btn-divider'></span>` to visually separate groups of buttons.

**Inside a `flex-toolbar`** — wrap the divider in a `<li>` with `aria-hidden='true'`:

```jsx
<li className='nav-item' aria-hidden='true'>
    <span className='btn-divider' />
</li>
```

**Inside a `btn-row`** (at the bottom of a section, between a grid and its actions):

```jsx
<span className='btn-divider'></span>
<div className='btn-row'>
    <button type='button' className='btn' onClick={handleAdd}>
        <span className='fa fa-fw fa-plus mr-2' aria-hidden={true}></span>Add
    </button>
    <button type='button' className='btn' disabled={selectedRows.length === 0} onClick={() => setShowDeleteLightbox(true)}>
        <span className='fa fa-fw fa-trash-can mr-2' aria-hidden={true}></span>Delete
    </button>
</div>
```

## Secure Platform — React UI Style Guide · 7. Buttons (cont. 3)
_chunk 572 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

Never use `<hr />` for this purpose — `btn-divider` is the platform standard and carries the correct spacing and colour via the shared stylesheet.

### New button with multiple types (dropdown)

When a feature supports creating multiple subtypes (e.g. an alert that can be Case, HR, Audit, etc.), replace the plain `New` button with a `DropDown` that exposes each type as a menu item. **Do not** add separate per-type buttons or pills elsewhere on the screen.

```jsx
import { DropDown } from '@shared/components/dropdown/dropdown.component';

<DropDown
    id='add-button'
    disableSelectorPadding
    selector={
        <button type='button' className='btn'>
            <span className='fa fa-plus mr-1'></span>
            {Constants.Add}
            <span className='ml-2 caret'></span>
        </button>
    }
>
    <ul className='pl-0'>
        {TypeOptions.map((opt) => (
            <li
                key={opt.value}
                id={'add-for-' + opt.value.toLowerCase()}
                className='pl-2 dropdown-item tw:hover:!bg-secure-blue-500-10 tw:!cursor-pointer'
                onClick={() => handleAddForType(opt.value)}
            >
                <span className={`fa ${opt.icon} mr-1`}></span>
                {opt.label}
            </li>
        ))}
    </ul>
</DropDown>

{/* Separate delete button */}
<button type='button' className='btn' disabled={selectedRecords.length === 0} onClick={handleDelete}>
    <span className='fa fa-trash mr-1'></span>
    {Constants.Delete}
</button>
```

Each option object in the constant should include an `icon` field:

```js
export const TypeOptions = [
    { value: 'Case',    label: 'Case',    icon: 'fa-file-alt' },
    { value: 'HR',      label: 'HR',      icon: 'fa-user-tie' },
    { value: 'Audit',   label: 'Audit',   icon: 'fa-clipboard-check' },
    { value: 'Service', label: 'Service', icon: 'fa-wrench' },
    { value: 'Task',    label: 'Task',    icon: 'fa-list-check' },
];
```

**Rules:**
- Pass the dropdown/button JSX to the `toolbar` prop on `PageLayout` — do not wrap in `<ul className='flex-toolbar'>` separately. `PageLayout` handles the wrapper.
- The `DropDown` selector uses `fa fa-plus` icon, the label `Add`, and a `<span className='caret'>` for the arrow.
- Plain action buttons (Edit, Delete, etc.) use `className='btn'`.
- Dropdown items use `pl-2 dropdown-item` classes with `fa fa-<icon> mr-1` for consistent icon spacing.
- Each dropdown `<li>` gets an `id` of `add-for-<type-value-lowercase>` for testability.
- Navigation passes the selected type via router state: `navigate('/admin/<feature>/new', { state: { system: value } })`.
- The detail form reads `useLocation().state?.system` to pre-populate the type field.
- `DropDown` handles outside-click, Escape key, and hover open/close automatically — do not re-implement this logic.

### CSS fix placement — bundle vs `new.ui.css`

`new.ui.css` is loaded by `_ThinLayout.cshtml` with no cache-busting querystring. PlatformUI's static file middleware caches it aggressively, so edits may not reach the browser for hours even after a hard-refresh.

**Rule: never rely on `new.ui.css` alone for a style fix. Always put the fix in a React bundle CSS file.**

React bundle CSS files are injected as `<style>` tags at runtime. Because they appear in the DOM *after* all `<link>` stylesheets, they win the cascade without needing `!important` (except when overriding a pre-existing `!important` rule from `new.ui.css`).

| Where the fix belongs | Examples |
|---|---|
| Global button behaviour | `toolbar.component.css` |
| Section title colour, adornment font resets | `section.component.css` |
| Feature-specific overrides | feature's own `*.module.css` or component CSS |

When you do need to update `new.ui.css`, add the same rule to a bundle CSS file as a reliable fallback.

---

## Secure Platform — React UI Style Guide · 8. Forms
_chunk 573 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

### Choosing the right input component

| What you see in the design | Component to use |
|---|---|
| Free text, URLs, keys, emails | `InputText` |
| Dots masking the value (e.g. `•••••••`) | `InputText` with `isPassword={true}` — not `type='password'` |
| A numeric value (e.g. `300`, `0`, `8529904`) | `InputNumber` with `hideSpinner={true}` |
| **Yes / No** (only two options) | `InputToggle` — never `LocalDataFilteredSelect` with Yes/No options |
| Dropdown with 3 or more distinct options | `LocalDataFilteredSelect` |

### InputText

**`onChange` passes the event object, not the value.** Always use `e.target.value` to extract the string.

```jsx
import { InputText } from '@shared/components/input-text/input-text.component';

<InputText
    id='first-name'
    id='first-name'
    label='First Name'
    value={form.firstName}
    onChange={(e) => setField('firstName', e.target.value)}
    value={form.firstName}
    onChange={(e) => setField('firstName', e.target.value)}
    placeholder='Enter first name'
    maxLength={100}
/>
```

### InputNumber

Use for any numeric field. Always add `hideSpinner={true}` and `containerClass='w-100'`. `onChange` passes the event object — use `parseInt(e.target.value)` or `parseFloat(e.target.value)`.

```jsx
import { InputNumber } from '@shared/components/input-number/input-number.component';

<InputNumber
    id='square-feet'
    label='Square Feet'
    value={form.squareFeet}
    onChange={(e) => setField('squareFeet', parseInt(e.target.value) || 0)}
    hideSpinner={true}
    containerClass='w-100'
/>
```

### InputToggle

Use for **all Yes/No fields** — never use `LocalDataFilteredSelect` with Yes/No options for boolean fields. `InputToggle` uses `topLabel` (not `label`). Value is boolean.

```jsx
import { InputToggle } from '@shared/components/input-toggle/input-toggle.component';

<InputToggle
    id='detail-inactive'
    topLabel='Inactive'
    value={form.inactive}
    onChange={() => setField('inactive', !form.inactive)}
/>
```

### DateTimePicker

Use for any date field. The component renders its own label, dropdowns (Day / Month / Year), and a calendar picker.

Add `fieldset` to wrap the component in the standard `form-group form-control-container` layout box — the same box every other input uses. **Do not manually wrap `DateTimePicker` in a `<fieldset>` — use the prop.**

```jsx
import DateTimePicker from '@shared/components/date-time-picker/date-time-picker.component';

<DateTimePicker
    fieldset
    id='store-open-date'
    label={IncidentConstants.StoreOpenDate}
    value={form.storeOpenDate}
    onChange={(val) => setField('storeOpenDate', val)}
/>
```

`onChange` receives an ISO-format date string (e.g. `'2026-04-13T00:00:00.00'`) or `null` when cleared. Store it as a string — do not convert to a `Date` object.

### Form layout pattern

```jsx
{/* Actions belong in the Toolbar — not at the bottom of the form */}
<Toolbar>
    <MotionButton idleLabel='Save' ... />
</Toolbar>

<Section title='Details'>
    <div className='row'>
        <div className='col-md-6 mb-3'>
            <InputText id='firstName' label='First Name' ... />
        </div>
        <div className='col-md-6 mb-3'>
            <InputText id='lastName' label='Last Name' ... />
        </div>
    </div>
    <div className='row'>
        <div className='col-12 mb-3'>
            <InputTextArea id='notes' label='Notes' ... />
        </div>
    </div>
</Section>
```

### Validation

**Always get `validationService` from the app context — never instantiate it locally.**

Each app provides a single `ValidationService` instance through its context (e.g. `IncidentContext`). Components consume it via `useContext`:

```jsx
import { useContext } from 'react';
import { IncidentContext } from '@incident/context';
import { Validation } from '@shared/models/validation.model';

export function MyDetailPage() {
    const { validationService } = useContext(IncidentContext);

    const handleSave = () => {
        if (!validationService.isGroupValid(VALIDATION_GROUP)) return;
        // proceed with save
    };

    return (
        <InputText
            id='my-field'
            label='My Field'
            value={form.myField}
            onChange={(e) => setField('myField', e.target.value)}
            validation={
                new Validation(VALIDATION_GROUP, validationService, [
                    () => validationService.validateNotEmpty(form.myField)
                ])
            }
        />
    );
}
```

## Secure Platform — React UI Style Guide · 8. Forms (cont. 2)
_chunk 574 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_


**Rules:**

1. **One instance per app, from context.** Do not call `new ValidationService()` in components — use the instance from the app context. The context file (`context.js`) creates the singleton at module level and provides it via `<AppProvider>`.
2. **Group names isolate validation scopes.** A single `ValidationService` instance can manage multiple independent form sections — each section uses a distinct group name (e.g. `'approve-form'`, `'reject-form'`). `isGroupValid(groupName)` only checks validators registered under that group, so there is no cross-scope leakage.
3. **Use `Validation` model to wire inputs.** Pass a `new Validation(groupId, validationService, [validatorFns])` to the `validation` prop of input components (`InputText`, `InputNumber`, `LocalDataFilteredSelect`, `DateTimePicker`, `FileUpload`, etc.). The component registers/unregisters itself automatically on mount/unmount.
4. **Call `isGroupValid` before submission.** This triggers all registered validators in the group and returns `false` if any fail. The input components display their own error messages — no manual error state management needed.
5. **Import `useContext` as a named import** — `import { useContext } from 'react'`. Never use `React.useContext()`.

**Common validators (methods on `ValidationService`):**

| Method | Use for |
|---|---|
| `validateNotEmpty(value)` | Required text fields — fails when value is empty or whitespace |
| `validateArrayNotEmpty(array)` | Required multi-select or file fields — fails when array is empty |
| `validateMin(value, min)` | Numeric minimum |
| `validateMax(value, max)` | Numeric maximum |
| `validateDateGreaterOrEqual(date, minDate, message)` | Date range constraints |

Each validator returns a `ValidationResponse` object (`{ valid, message }`). For custom validators, return `new ValidationResponse(isValid, errorMessage)`.

**Test pattern — mock via context Provider:**

```jsx
jest.mock('<relative-path>/context', () => {
    const React = require('react');
    const IncidentContext = React.createContext({});
    return { IncidentContext };
});

const mockValidationService = {
    isGroupValid: jest.fn(() => true),
    validateNotEmpty: jest.fn(() => ({ valid: true, message: null }))
};

const { IncidentContext } = require('<relative-path>/context');

const renderComponent = () =>
    render(
        <IncidentContext.Provider value={{ validationService: mockValidationService }}>
            <MyComponent />
        </IncidentContext.Provider>
    );
```

To test the validation-failure path, mock `isGroupValid` to return `false` before the specific test:

```jsx
it('should not save when validation fails', () => {
    mockValidationService.isGroupValid.mockReturnValueOnce(false);
    renderComponent();
    fireEvent.click(screen.getByText('Save'));
    expect(MyService.save).not.toHaveBeenCalled();
});
```

### AlertBox vs cpf.alert()

**Use `AlertBox`** for persistent, baked-in warnings on the page (e.g., AI content disclaimers):

```jsx
import { AlertBox } from '@shared/components/alert-box/alert-box.component';

<AlertBox messageType='warning' message={IncidentConstants.AiContentDisclaimer} />

{this.state.validationError && (
    <AlertBox messageType='danger' message={IncidentConstants.FormValidationFailed} />
)}
```

Place `AlertBox` at the **top of the relevant Section**. `messageType` options: `'danger'`, `'warning'`, `'info'` (default).

**Use `cpf.alert()`** for transient toast notifications after operations complete (save, delete, etc.):

```js
cpf.alert(IncidentConstants.SavedSuccessfully, 's');     // success — green
cpf.alert(IncidentConstants.SaveFailed, 'e');            // error — red
cpf.alert(IncidentConstants.DeletedSuccessfully, 's');   // success
```

**Always resource all message text** in `constants.js` — never hardcode strings.

Call it after the operation succeeds, before or after navigating away:

```js
function handleSave() {
    SettingsService.save(form).then(() => {
        cpf.alert(IncidentConstants.SettingsSavedSuccessfully, 's');
        navigate('/admin');
    });
}

function handleDelete() {
    setItems((prev) => prev.filter((i) => i.id !== selectedId)); // optimistic
    ItemService.delete(selectedId);
    cpf.alert(IncidentConstants.DeletedSuccessfully, 's');
}
```

---

## Secure Platform — React UI Style Guide · 9. Common Gotchas
_chunk 575 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

### LocalDataFilteredSelect — value is an array, not a string

`FilteredSelect` (and its wrapper `LocalDataFilteredSelect`) expects `value` to be an **array of option objects** and calls `onChange` with an array. Passing a plain string crashes with `this.props.value.map is not a function`.

Always use the two helpers below to convert between your string form state and the component's array API:

```js
/** Convert a scalar form value to the array FilteredSelect expects. */
function toSelectValue(options, value) {
    if (!value) return [];
    const found = options.find((o) => o.value === value);
    return found ? [found] : [];
}

/** Extract a scalar string from FilteredSelect's array onChange payload. */
function fromSelectValue(selected) {
    return Array.isArray(selected) ? (selected[0]?.value ?? '') : (selected ?? '');
}
```

Usage:

```jsx
<LocalDataFilteredSelect
    id='detail-status'
    label='Status'
    value={toSelectValue(StatusOptions, form.status)}
    options={StatusOptions}
    onChange={(selected) => setField('status', fromSelectValue(selected))}
/>
```

**In tests**, mock `LocalDataFilteredSelect` to extract the scalar from the array value so `.value` checks still work:

```jsx
LocalDataFilteredSelect: ({ id, label, value, onChange, disabled, options }) => {
    const displayVal = Array.isArray(value) ? (value[0]?.value ?? '') : (value ?? '');
    return (
        <select id={id} value={displayVal} onChange={(e) => onChange(e.target.value)} disabled={disabled}>
            {options.map((o, i) => <option key={i} value={o.value}>{o.label}</option>)}
        </select>
    );
},
```

---

### Icon-only buttons — `btn btn-fa`, not `btn btn-danger btn-fa`

`btn-fa` sizes and shapes an icon-only circular button. Do **not** add `btn-danger` unless the action is genuinely destructive (permanent data loss). Delete buttons inside condition builders and reorderable lists are not destructive enough to warrant red — use `btn btn-fa` and let the trash icon communicate the action.

```jsx
{/* Correct — blue platform style */}
<button className='btn btn-fa' onClick={handleDelete}>
    <span className='fa fa-fw fa-trash' />
</button>

{/* Only use btn-danger for permanent/irreversible actions */}
<button className='btn btn-danger'>Delete Record</button>
```

---

### Section headings inside tabs — use `div.fw-semibold`, not `<h6>`

`<h6>` inherits `color: var(--secure-primary-text)` from the theme, rendering as dark blue. For column/panel headings within a tab body use:

```jsx
<div className='fw-semibold mb-3' style={{ color: 'var(--default-text)' }}>
    Conditions
</div>
```

This gives the correct black body-text colour without fighting the theme heading styles.

---

### Single `<Section>` per tab for multi-column layouts

Wrapping each column in its own `<Section>` creates two separate white cards with a visible gap between them. Wrap both columns in a single `<Section>` so the tab body is one unified card:

```jsx
{activeTab === 'my-tab' && (
    <Section>
        <div className='row'>
            <div className='col-md-6'>{ /* left panel */ }</div>
            <div className='col-md-6'>{ /* right panel */ }</div>
        </div>
    </Section>
)}
```

---

### AND/OR condition group bracket

Use a single `div` with a three-sided border (`borderTop + borderLeft + borderBottom`) and an absolutely-centred badge. Do **not** build the bracket from 5 separate corner + line divs — they misalign.

```jsx
<div
    style={{
        borderTop: '2px solid var(--primary-base)',
        borderLeft: '2px solid var(--primary-base)',
        borderBottom: '2px solid var(--primary-base)',
        borderRadius: '4px 0 0 4px',
        width: '18px',
        marginRight: '8px',
        flexShrink: 0,
        position: 'relative',
        alignSelf: 'stretch',
    }}
>
    <span
        className='badge rounded-pill'
        style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            background: 'var(--primary-light)',
            color: 'var(--secure-primary-text)',
            fontSize: '0.65rem',
            whiteSpace: 'nowrap',
        }}
    >
        AND
    </span>
</div>
```

---

### Floating pill picker (field / operator / value selectors)

## Secure Platform — React UI Style Guide · 9. Common Gotchas (cont. 2)
_chunk 576 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

For condition builders where a full-width `LocalDataFilteredSelect` would be too large inline, use the pill-picker pattern: a `badge rounded-pill` button that opens an absolutely-positioned floating panel.

```jsx
<div style={{ position: 'relative' }}>
    {/* Trigger pill */}
    <button
        type='button'
        id='cond-field-1'
        className='badge rounded-pill fw-normal'
        style={{
            background: value ? 'var(--primary-light)' : 'var(--bs-gray-200, #e9ecef)',
            color: value ? 'var(--secure-primary-text)' : 'var(--bs-secondary-color, #6c757d)',
            border: 'none',
            cursor: 'pointer',
            padding: '0.4rem 0.85rem',
            fontSize: '0.85rem',
        }}
        onClick={() => setOpen((prev) => !prev)}
    >
        {value || 'Nothing selected'}
    </button>

    {/* Floating panel */}
    {open && (
        <div
            id='field-picker-1'
            style={{
                position: 'absolute',
                top: 'calc(100% + 6px)',
                left: 0,
                zIndex: 1050,
                background: 'white',
                border: '1px solid rgba(0,0,0,0.1)',
                borderRadius: '8px',
                padding: '0.75rem',
                minWidth: '22rem',
                boxShadow: '0 4px 20px rgba(0,0,0,0.12)',
            }}
        >
            { /* search input + list */ }
        </div>
    )}
</div>
```

Close on outside click with a `useEffect`:

```js
useEffect(() => {
    if (!openPickerId) return;
    function onMouseDown(e) {
        const el = document.getElementById(`field-picker-${openPickerId}`);
        if (el && !el.contains(e.target)) setOpenPickerId(null);
    }
    document.addEventListener('mousedown', onMouseDown);
    return () => document.removeEventListener('mousedown', onMouseDown);
}, [openPickerId]);
```

---

### Optimistic local state for lists (delete / add / reorder)

When a component manages a list that can be deleted from, added to, or reordered, **do not rely on refetch to update the UI**. Use local state instead:

```js
const [localItems, setLocalItems] = useState([]);

// Sync from query — depend on the inner data reference, not the query result object,
// to avoid resetting local state on every render.
useEffect(() => {
    setLocalItems(queryData?.data ?? []);
}, [queryData?.data]); // eslint-disable-line react-hooks/exhaustive-deps

function handleDelete(item) {
    setLocalItems((prev) => prev.filter((i) => i.id !== item.id)); // optimistic
    Service.deleteItem(item.id);                                    // fire-and-forget
}

function handleAdd(newItem) {
    setLocalItems((prev) => [...prev, { id: nextIdRef.current++, ...newItem }]); // optimistic
    setInputValue('');
    Service.addItem(newItem);
}
```

> **Why `queryData?.data` as the dependency?** The query result object (`queryData`) is a new reference on every render when mocked. Using `queryData?.data` (the stable inner array) means the effect only re-runs when the server actually returns new data — not after every local state update.

---

### Drag-and-drop reordering (HTML5 native, no library)

No DnD library is installed. Use the browser's built-in drag API:

```jsx
const dragIndexRef = useRef(null);
const [dragOverIndex, setDragOverIndex] = useState(null);

{items.map((item, index) => (
    <tr
        key={item.id}
        draggable
        className={dragOverIndex === index ? 'table-active' : ''}
        onDragStart={() => { dragIndexRef.current = index; }}
        onDragOver={(e) => { e.preventDefault(); setDragOverIndex(index); }}
        onDrop={(e) => {
            e.preventDefault();
            const from = dragIndexRef.current;
            if (from !== null && from !== index) {
                setItems((prev) => {
                    const next = [...prev];
                    const [item] = next.splice(from, 1);
                    next.splice(index, 0, item);
                    return next;
                });
            }
            dragIndexRef.current = null;
            setDragOverIndex(null);
        }}
        onDragEnd={() => { dragIndexRef.current = null; setDragOverIndex(null); }}
    >
        <td style={{ cursor: 'grab' }}>
            <span className='fa fa-fw fa-grip-vertical text-muted' />
        </td>
        { /* other cells */ }
    </tr>
))}
```

## Secure Platform — React UI Style Guide · 9. Common Gotchas (cont. 3)
_chunk 577 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

`dragIndexRef` is a `useRef` (not `useState`) because the drag source index does not need to trigger a re-render. `dragOverIndex` is `useState` so the hover highlight updates reactively.

---

### ParameterBox — layout rules

`ParameterBox` is the standard filter bar for list and dashboard pages. It renders as a dark horizontal container (the `box` class) with `Parameter` children inline and Apply/Reset buttons at the end — matching the Executive Workbench style.

**Never wrap `ParameterBox` in a `col-md-X` div.** A column constraint collapses the flex container to a vertical strip and pushes the Apply/Reset buttons below the parameters instead of keeping them inline to the right.

```jsx
{/* Correct — content-width filter bar */}
<div className='tw:w-fit mb-3'>
    <ParameterBox onApply={apply} onReset={reset}>
        <Parameter id='my-param-viewing' title={MyConstants.Viewing} selectedValue={...}>
            {/* filter control */}
        </Parameter>
        <Parameter id='my-param-date' title={MyConstants.DateRange} selectedValue={...}>
            {/* filter control */}
        </Parameter>
    </ParameterBox>
</div>

{/* Wrong — column constraint makes ParameterBox narrow and vertical */}
<div className='col-md-4'>
    <ParameterBox onApply={apply} onReset={reset}>
        ...
    </ParameterBox>
</div>
```

Use `d-inline-flex` on the outer div so the dark box wraps its content width rather than stretching across the page. If you want the bar to span a fixed proportion of the page, use a Tailwind width class (`tw:w-1/2`, etc.) rather than a Bootstrap column.

---

### Toolbar icon margin — use `mr-2`, not `mr-3`

Icons inside toolbar `<a className='btn'>` or `<button className='btn'>` elements use `mr-2` for the gap between the icon and its label. `mr-3` is too wide and looks visually heavier than the rest of the platform toolbar.

```jsx
{/* Correct */}
<a href='#' className='btn' onClick={...}>
    <span className='fa fa-fw fa-plus mr-2' aria-hidden={true}></span>
    {IncidentConstants.NewIncident}
</a>

{/* Wrong — mr-3 creates oversized icon margin */}
<a href='#' className='btn' onClick={...}>
    <span className='fa fa-fw fa-plus mr-3' aria-hidden={true}></span>
    {IncidentConstants.NewIncident}
</a>
```

---

### All visible strings must be resourced in constants — never hardcode labels

Every user-visible string (column headers, parameter titles, dropdown option labels, button text, input placeholders, section titles, confirmation messages) must be declared as a constant using the `RESOURCE{{...}}` format and referenced by name in JSX. Hardcoded strings bypass translation and make search-and-replace impossible.

**The RESOURCE format:**

```js
// src/apps/incident/constants.js — root app constants file
export const IncidentConstants = {
    CaseNumber: 'RESOURCE{{Sysrepublic.Secure.UI.Areas.Incident.IncidentResources}:{CaseNumber}:{Case Number}}',
    DeleteConfirm: 'RESOURCE{{Sysrepublic.Secure.UI.Areas.Incident.IncidentResources}:{DeleteConfirm}:{Are you sure you want to delete this record?}}',
};
```

The three parts of the token are `{ResourceFile}:{Key}:{DisplayValue}`. The display value is what renders in the UI before translation is applied.

**Where to add new constants:**

Add all constants to the **root app constants file** (e.g., `src/apps/incident/constants.js`), never to a separate page-scoped `constants.js`. Group them under comment blocks by feature:

```js
// MyFeature — List
MyFeaturePageTitle: 'RESOURCE{{...}:{MyFeaturePageTitle}:{My Feature}}',
MyFeatureDeleteConfirmTitle: 'RESOURCE{{...}:{MyFeatureDeleteConfirmTitle}:{Delete Record}}',

// MyFeature — Detail
MyFeatureGeneralInfo: 'RESOURCE{{...}:{MyFeatureGeneralInfo}:{General Information}}',
```

This keeps all strings in one place for translation and consistency across the app.

```jsx
{/* Correct */}
const CUSTOM_HEADER_NAMES = {
    caseNumber: IncidentConstants.CaseNumber,
    caseStatus: IncidentConstants.CaseStatus,
};

options={[
    { value: 'active', label: IncidentConstants.ActiveIncidents },
    { value: 'closed', label: IncidentConstants.ClosedIncidents },
]}

<input placeholder={IncidentConstants.SearchIncident} ... />

{/* Wrong — hardcoded strings */}
const CUSTOM_HEADER_NAMES = {
    caseNumber: 'Case Number',
    caseStatus: 'Case Status',
};

options={[
    { value: 'active', label: 'Active Incidents' },
    { value: 'closed', label: 'Closed Incidents' },
]}

<input placeholder='Search incidents...' ... />
```

## Secure Platform — React UI Style Guide · 9. Common Gotchas (cont. 4)
_chunk 578 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_


If the constant does not exist yet, add it to `constants.js` before using it — never inline the string as a workaround.

**No colons in RESOURCE fallback text.** Never include a trailing colon (`:`) in the English fallback portion of a RESOURCE string. Colons are layout punctuation — they belong in CSS (`::after`) or the label component, not in the resource value. `Label: 'RESOURCE{{...}:{Label}:{Name:}}'` is wrong; `Label: 'RESOURCE{{...}:{Label}:{Name}}'` is correct.

---

### Form state — single `handleChange` function

Use one generic `handleChange(field, value)` instead of one setter per field. This scales cleanly to any number of fields and avoids a proliferation of `setX` callbacks.

```js
const [form, setForm] = useState(INITIAL_STATE);

function handleChange(field, value) {
    setForm((prev) => ({ ...prev, [field]: value }));
}
```

```jsx
<InputText
    id='store-name'
    label={IncidentConstants.StoreName}
    value={form.storeName}
    onChange={(e) => handleChange('storeName', e.target.value)}
/>
<InputToggle
    id='detail-inactive'
    topLabel={IncidentConstants.Inactive}
    value={form.inactive}
    onChange={() => handleChange('inactive', !form.inactive)}
/>
```

---

### Never wrap functional components with `withRouter`

`withRouter` is a class-component pattern from React Router v4/v5. Functional components use hooks directly — `useNavigate`, `useParams`, `useLocation`. Wrapping a functional component with `withRouter` is redundant and masks the fact that routing hooks are available.

```jsx
{/* Correct — hook directly in the function body */}
export function MyPage() {
    const navigate = useNavigate();
    const { id } = useParams();
    ...
}

{/* Wrong */}
export default withRouter(MyPage);
```

---

### Element IDs — kebab-case, lowercase only

All `id` attributes must be **kebab-case and lowercase**. Never use camelCase, PascalCase, or underscores.

```jsx
{/* Correct */}
<button type='button' id='toolbar-delete' />
<input id='store-open-date' />

{/* Wrong */}
<button type='button' id='toolbarDelete' />
<input id='StoreOpenDate' />
```

This applies to toolbar buttons, form inputs, grid IDs, tab links, and any element referenced in tests.

---

### Navigation — always use explicit paths, not `navigate(-1)`

Always pass an explicit path to `navigate`. Never use `navigate(-1)` — browser history is unreliable in hash-based routing and cannot be tested deterministically.

```jsx
{/* Correct */}
navigate('/admin/locations');

{/* Wrong — do not use */}
navigate(-1);
```

---

## Secure Platform — React UI Style Guide · 10. Data Display
_chunk 579 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

### InfoTile / FancyInfoTile

Use `InfoTile` for key metric cards at the top of dashboard-style screens.

```jsx
import { InfoTile } from '@shared/components/info-tile/info-tile.component';

<div className='row mb-3'>
    <div className='col-md-4'>
        <InfoTile
            id='total-cases'
            title={{ label: 'Total Cases', colour: 'var(--secure-primary-text)' }}
            mainValue={this.state.totalCases}
            subValue='This month'
            footerValue='View all'
            style='subtleaccent'
            link='/cases'
        />
    </div>
</div>
```

`style` options: `'subtleaccent'`, `'success'`, `'danger'`, `'warning'`, `'white'`.

Use `skeleton={true}` while data is loading — `InfoTile` handles its own skeleton state.

### DataGrid

Use `LocalDataDataGrid` for tabular data. Never build custom `<table>` markup.

**Standard list screen grid configuration:**

Use `LocalDataDataGrid` directly — do not wrap it in a `<Section>`. Pass `title` to the grid and let the built-in header handle filtering. Do not add a custom filter bar — the grid's native search is sufficient and adding one duplicates the UI.

Wrap the grid in a `tw:min-h-0` div and set `tw:flex tw:flex-col` on the `page-content` root. This lets the grid fill the remaining viewport height correctly on all screen sizes.

```jsx
<div className='page-content tw:flex tw:flex-col'>
    {/* portals: Toolbar, Compass, PageTitle */}

    <div className='tw:min-h-0'>
        <LocalDataDataGrid
            id='feature-grid'
            key={gridKey}
            title='Record Title'
            data={gridData}
            columnsToShow={FeatureColumnsToShow}
            showAllResults={false}
            showSorting={true}
            showCheckboxes={true}
            allowMultipleSelection={true}
            checkboxSelectionChanged={setSelectedRecords}
            rowClicked={(row) => {
                const id = row.id?.rawValue ?? row.id;
                navigate('/admin/<feature>/' + id);
            }}
        />
    </div>
</div>
```

**Rules:**
- **Do not** wrap the grid in a `<Section>` — use `LocalDataDataGrid` directly.
- Pass `title` directly to `LocalDataDataGrid` — do not set it on a surrounding `Section`.
- **Do not** pass `showHeader={false}` — the grid's built-in header renders the title and native search correctly.
- **Do not** add a custom filter bar via `headerActions` or elsewhere — the grid's built-in search handles filtering natively. Adding one duplicates the search box.
- Build `gridData` from the full data array — do not pre-filter before passing to the grid.
- Always add `tw:flex tw:flex-col` to the `page-content` root and wrap the grid in `<div className='tw:min-h-0'>` for correct viewport height behaviour.
- Filter data before building `gridData`; pass already-filtered data into the grid.
- Always pass `showCheckboxes={true}` and `allowMultipleSelection={true}` so users can multi-select for bulk actions.
- Always pass `rowClicked` — clicking a row navigates directly to the detail/edit screen.
- Toolbar Edit/Delete buttons remain for users who prefer keyboard-driven workflows; they operate on `selectedRecords` set by `checkboxSelectionChanged`.
- `rowClicked` receives **one argument** — `(row)` — not `(event, row)`. The DataGrid calls `props.rowClicked(row)` internally; the event is not forwarded. Writing `(e, row) => ...` silently breaks navigation because `e` becomes the row and `row` is `undefined`.
- Row IDs from `rowClicked` arrive as `row.id?.rawValue ?? row.id` because the DataGrid wraps raw values in `{ rawValue, cellValue, ... }` objects.
- In tests, mock `rowClicked` the same way: `onClick={() => rowClicked(item)}` — not `onClick={(e) => rowClicked(e, item)}`.

**camelCase data keys and `customHeaderNames`:**

All data objects passed to the grid must use camelCase property keys — never quoted multi-word keys like `'Store No'` or `'Case Number'`. This is standard JS. The grid uses the `columnsToShow` values as both data-object keys and column header text by default. When the display header differs from the key name, use `customHeaderNames` to decouple them:

```jsx
// Data objects — always camelCase
const gridData = items.map((item) => ({
    id: item.id,
    caseNumber: item.caseNumber,
    caseStatus: item.caseStatus,
    assignedTo: item.assignedTo
}));

// columnsToShow — matches the camelCase data keys
const ColumnsToShow = ['caseNumber', 'caseStatus', 'assignedTo'];

## Secure Platform — React UI Style Guide · 10. Data Display (cont. 2)
_chunk 580 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

// customHeaderNames — maps each key to its display string via constants
const HEADER_NAMES = {
    caseNumber: IncidentConstants.CaseNumber,
    caseStatus: IncidentConstants.CaseStatus,
    assignedTo: IncidentConstants.AssignedTo
};

<LocalDataDataGrid
    data={gridData}
    columnsToShow={ColumnsToShow}
    customHeaderNames={HEADER_NAMES}
    ...
/>
```

Never use quoted keys with spaces (`'Case Number'`) anywhere in the data pipeline — not in the data objects, not in `columnsToShow`, not in `customHeaderNames`. All three must use camelCase keys consistently.

### Skeleton

Use `Skeleton` for loading placeholders on any element that waits for async data:

```jsx
import { Skeleton } from '@shared/components/skeleton/skeleton.component';

{this.state.loading ? (
    <Skeleton width='100%' height='200px' />
) : (
    { /* actual content */ }
)}
```

### Lightbox (modal)

Use `Lightbox` for confirmations, detail panels, and forms that shouldn't navigate away.

```jsx
import { Lightbox } from '@shared/components/lightbox/lightbox.component';

{this.state.showModal && (
    <Lightbox
        title='Confirm Delete'
        onSuccess={() => this.delete()}
        onDismiss={() => this.setState({ showModal: false })}
        width='500px'
    >
        Are you sure you want to delete this item?
    </Lightbox>
)}
```

Lightbox handles Enter (confirm) and Escape (dismiss) keyboard shortcuts automatically.

---

## Secure Platform — React UI Style Guide · 11. Dark Mode
_chunk 581 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

The `.dark-theme` class on `<html>` activates dark mode — all theme tokens switch automatically.

**Rules for new components:**
1. Only use theme tokens for color — never hardcode hex values.
2. If you need a color that has no existing token, check if a semantically similar token exists before adding a new one.
3. If you must add a new token, add both the light value to the `:root` block and the dark override to the `.dark-theme` block in `theme.css`.
4. To test dark mode locally: add `class="dark-theme"` to `<html>` in the browser DevTools.

---

## Secure Platform — React UI Style Guide · 12. File Structure for a New App
_chunk 582 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

```
src/apps/my-feature/
├── index.js              # Router and app entry point
├── constants.js          # All string literals (labels, messages, etc.)
├── context.js            # React Context (only if shared state is needed)
├── pages/
│   ├── list.component.js       # List page
│   ├── list.component.test.js
│   ├── details.component.js    # Detail/edit page
│   └── details.component.test.js
├── components/           # Feature-specific components (not shared)
│   └── my-toolbar.component.js
└── services/
    └── my-feature.service.js
```

All string literals go in `constants.js` — no inline string literals in JSX.

```js
// constants.js
export const MyFeatureConstants = {
    PageTitle: 'My Feature',
    SaveButton: 'Save',
    SaveSuccessMessage: 'Saved successfully.',
    SaveErrorMessage: 'Failed to save. Please try again.'
};
```

---

## Secure Platform — React UI Style Guide · 12. Admin Page Registration
_chunk 583 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

When adding a new admin feature page (e.g., `admin-locations`, `admin-smart-alerts`), register it in the admin dashboard:

The admin page uses `AdminCategoryCard` components with grouped links, not individual `InfoTile` tiles.

To add a new admin link:
1. Find the appropriate category in the `getCategories()` function in `src/apps/incident/pages/admin/admin.component.js`
2. Add `{ label: IncidentConstants.<ConstantName>, href: '#/admin/<feature-name>' }` to its `links` array
3. Update the admin snapshot test

---

## Secure Platform — React UI Style Guide · 13. Component Checklist for New Screens
_chunk 584 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/style-guide.md_

Before marking a screen complete, verify:

- [ ] Root element is `<div className='page-content'>`
- [ ] `PageTitle` sets `documentTitle`
- [ ] All action buttons (Save, Delete) are in the `<Toolbar>`, not at the bottom of a form
- [ ] Multi-tab detail pages use `NavLink` + `<Outlet>` + child routes — not `activeTab` state + conditional JSX
- [ ] Every `<Section>` has a `title` prop — no raw `<div>` headings
- [ ] Panel sub-headers inside a section use `color: var(--secure-primary-text)`, `fontWeight: bold`
- [ ] All async buttons use `MotionButton` with loading/success/error states
- [ ] All colors use CSS custom property tokens
- [ ] No hardcoded hex values or pixel spacing in component CSS
- [ ] All icons use `<span className='fa fa-fw fa-<name>' />` pattern
- [ ] All string literals live in `constants.js`
- [ ] `AlertBox` is used for error/warning states (not inline text)
- [ ] `Skeleton` is used while data loads
- [ ] Dark mode works (test with `.dark-theme` on `<html>`)
- [ ] PropTypes defined for every prop
- [ ] Unit tests cover happy path, empty state, and error state
- [ ] Any shared components (`Sources/UI/Components/src/_react/src/shared/components/`) changed must have unit tests covering the change

## Transaction Vault · Overview
_chunk 585 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

The **Transaction Vault** is the system Secure uses to look up full receipt data — the complete ARDM JSON for a single POS transaction (header, line items, tenders, discounts, loyalty, etc.). It powers the Transaction Viewer, receipt drill-downs, and anything else that needs the full detail of an individual transaction.

Physically, the current implementation is **Azure Table Storage**, fronted by the **Data API** (historically "Receipt API") and reached from Secure through the `TableStorageEventProvider`. Older transactions still sit in Greenplum and are served by the `GenericEventProvider` fallback.

This doc describes the provider architecture, the HTTP contract, how the cut-off date splits traffic, and the fallback chain.

> **Not to be confused with** bulk analytical queries against POS data. Searches that aggregate transactions run against ARDM in Snowflake/Greenplum via the search pipeline — see `search.md` and `../databases/snowflake.md`. The Transaction Vault is for fetching *one specific receipt at a time*.

For the historical design context see:
- [Azure Table Storage for ARDM JSON — Secure Implementation](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475882520601/Azure+Table+Storage+for+ARDM+JSON+-+Secure+Implementation)
- [Data API / Receipt API for local development](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/476436627469/Data+Api+Receipt+API+for+local+development)
- [Data API / Receipt API usage](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/476720300042/Data+Api+Receipt+API+usage)

---

## Transaction Vault · Event providers
_chunk 586 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

Event providers are Secure's abstraction for "get me the details of these journal events". They're configured per source app (`store`, `ecomm`, `inventory`) via `EventProvider.{sourceApp}` config items, with `EventProviderFactory` instantiating the configured type at runtime.

| Provider | Where the data lives | When it's used |
|---|---|---|
| `TableStorageEventProvider` | Azure Table Storage (via Data API) | Default for ARDM; current transactions |
| `GenericEventProvider` | Greenplum / Snowflake (via SQL procs) | Fallback for older transactions, or when the API is unavailable |
| `SqlServerEventProvider` | SQL Server | CRDM (legacy pre-ARDM) |

Which provider wins is controlled by the `name` field in the `EventProvider.{sourceApp}` JSON config plus feature flags.

---

## Transaction Vault · Architecture
_chunk 587 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

```
Transaction Viewer / search drill-down
    ↓
IEventProvider (abstract)
    ↓ constructed by EventProviderFactory
TableStorageEventProvider
    ↓
    │  if transaction >= DataApi.CutOffDate
    ├────────────────────────────────────┐
    ↓                                    ↓
IArdmJsonApi (Refit)                  Fallback
    ↓                                    ↓
HTTPS + Basic Auth            ┌──────────┴──────────┐
    ↓                          ↓                     ↓
Data API                 GenericEventProvider   Snowflake scalar/
    ↓                    (Greenplum)             table function
Azure Table Storage
(ARDM JSON per txn)
```

**Key files:**
- `Sources/Core/Core/Event Providers/TableStorageEventProvider.cs` — main provider
- `Sources/Core/Core/Event Providers/GenericEventProvider.cs` — base class and fallback target
- `Sources/Core/Core/Event Providers/EventProviderFactory.cs` — constructs the configured provider
- `ApprissRetail.Secure.Common.Api.IArdmJsonApi` — Refit interface for the Data API

---

## Transaction Vault · What the Data API returns
_chunk 588 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

One transaction's full ARDM JSON. For store transactions the payload is keyed by a flat header plus arrays of `item`, `tender`, `itemdiscount`, `transactiondiscount`, etc. For e-commerce the equivalent order-shaped JSON.

### HTTP contract

| Endpoint | Purpose |
|---|---|
| `GET /transaction/{clientId}/{transactionId}` | One store transaction |
| `GET /order/{clientId}/{orderId}` | One e-commerce order |
| `POST /transactions/{clientId}` (batched) | Multiple store transactions in one call — gated by `Feature.DataApi.EnableBatchedEventSummariesEndpoint` |

Authentication is HTTP Basic; the client is generated by Refit against `IArdmJsonApi` with an `AuthorizationHeaderHandler`.

Example production base URLs:
- US: `https://prd-data-api-wus2.apprissretailcloud.com`
- EU: `https://prd-data-api-neu.apprissretailcloud.com`

---

## Transaction Vault · Provider operations
_chunk 589 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

The provider implements three read operations, all overriding `GenericEventProvider`:

| Method | Returns |
|---|---|
| `GetJournalEventDetails(eventIds, ct)` | Raw ARDM JSON strings, one per event |
| `GetJournalEventSummaries(eventIds, order, ct)` | Summarised `JObject` per event — only the fields listed in `DataApi.EventSummaryFields` |
| `GetJournalEventSummariesAndDetails(eventIds, conn, order, ct)` | Both in one call |

Summaries are built by `BuildEventSummary` — a case-insensitive projection over the configured field list (e.g. `transactionid`, `storeno`, `cashierno`, `ticketamount`, `starttransdatetime`, `endtransdatetime` by default for store). This lets the UI render transaction lists cheaply without deserialising the full payload.

### Per-event vs batched

Per-event fan-out uses `Parallel.ForEach` with `MaxDegreeOfParallelism = 3` to fetch events concurrently.

Batched requests send the list of IDs to a single endpoint and validate `requested_count == found_transactions`, raising on mismatch and exposing the `missing_transactions` list in the exception message.

---

## Transaction Vault · Cut-off date routing
_chunk 590 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

`DataApi.CutOffDate` (ISO date string, e.g. `2025-08-01`) splits traffic. `IsEventInTableStorage(eventId)` parses the first 6 or 8 characters of the event ID as a date and compares it against the cut-off:

- **On or after** the cut-off → Data API
- **Before** the cut-off → fallback (Greenplum by default)

If the cut-off date isn't configured, it defaults to three months before the current UTC time. Separate cut-off items exist per source app (`DataApi.CutOffDate` for store, `DataApi.CutOffDate.Ecomm` for e-commerce).

---

## Transaction Vault · Fallback chain
_chunk 591 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

Every call has up to two fallback paths, picked up when the primary fails or the cut-off says to skip the API:

1. **Snowflake** — if `Feature.DataApi.EnableFallbackToSnowflakeEventProvider` is on, the provider calls a Snowflake scalar/table function (`GET_TRANSACTION_JSON`, `GET_ORDER_JSON`) over the `Snowflake.EventProvider.FallbackConnectionName` connection (default `pos-data`). Used primarily for Snowflake-only clients where there's no Greenplum to fall back to.
2. **Greenplum** (the standalone `GenericEventProvider`) — if `Feature.DataApi.EnableFallbackToGenericEventProvider` is on (default true). Configured via `DataApi.FallbackConnectionName`.

A **standalone** `GenericEventProvider` instance is constructed at startup for each fallback so calls don't virtual-dispatch back into `TableStorageEventProvider` (which would re-enter the cut-off check and loop).

On success, response debug headers include:
- `Eventsource`: the provider that actually served the data (e.g. `TableStorageEventProvider`, `GenericEventProvider`, `SnowflakeFunction`)
- `Eventinfo`: how long the lookup took

These make it visible in the browser's network panel which backend served a given receipt — useful for debugging cut-off and fallback behaviour in place.

---

## Transaction Vault · Snowflake fallback function — per-client overrides
_chunk 592 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

When the Snowflake fallback path runs, it calls a scalar function `GET_TRANSACTION_JSON(TXN_ID NUMBER)` on the client's Secure schema (`$(SnowflakeSecureClientSchemaName)`, e.g. `C164_COP`). The function returns a `VARIANT` shaped to match the Data API / Greenplum JSON contract: a flat header merged with `REFERENCE_LOCATION`, plus arrays for `item`, `tender`, `itemdiscount`, `transactiondiscount`, `loyaltycard`, `customer`, `giftcard`, `ageinformation`, `operatoraction`, `recalledtransaction`, and an `employee` lookup against `REFERENCE_EMPLOYEE`.

The Snowflake source is in `Sources/Databases/Snowflake/Programmability/Snowflake/`:

| Path | Purpose |
|---|---|
| `ArdmDependent/Common/Functions/secure/GetTransactionJson.sql` | Base / fallback. Used for any client without a per-client override. |
| `ClientSpecific/<id>/ArdmDependent/Common/Functions/secure/GetTransactionJson.sql` | Per-client override. Lunar deploys this in place of the base for that client only. |

Lunar resolves overrides by client ID, so adding a `ClientSpecific/<id>/…/GetTransactionJson.sql` file is enough to swap the implementation for a single tenant.

### Why per-client overrides exist

The Greenplum equivalent (`secure.get_secure_json` and friends) was forked per client over time. Common deviations baked into individual versions:

- extra collections on the JSON root (e.g. `pettycash_ext`, `pointscoupon`, `event`, `linkedorder`)
- `discountstaffid` resolved against `REFERENCE_EMPLOYEE` rather than passed through from the header
- a second `REFERENCE_EMPLOYEE` lookup populating `purchasingemployee`
- `origtendertypes` derived from `recalledtransaction` joined back to `tender`
- some clients omitting whole collections that the base ships
- the PL/pgSQL `json_object_agg` UNION ALL merge pattern (all keys flat) — needs sanity checking against the Snowflake `OBJECT_INSERT` shape

Each Snowflake override carries a header comment naming the source GP cluster + schema (e.g. `Source GP cluster(s): GP9:ardm_010`) and a `Deviations from the standard get_secure_json that are NOT yet translated` block listing whatever still needs manual review.

### `_row_created` and the `EXCLUDE` clauses

The base override uses two patterns to drop columns the GP-replicated tables carry but the JSON contract doesn't:

- `OBJECT_DELETE(OBJECT_CONSTRUCT_KEEP_NULL(*), '_row_created')` — strips the SnowTime ingest marker
- `rl.* EXCLUDE (_row_created, inserteddatetime, updateddatetime, …)` — avoids duplicate column names when joining `ARDM_HEADER` with `REFERENCE_LOCATION`

Tables that are loaded **directly** into Snowflake (i.e. not replicated through the GP → SnowTime path) don't carry `_row_created` at all. For overrides pointed at those tables, drop the `OBJECT_DELETE(..., '_row_created')` wrappers, but keep an `EXCLUDE` on the `REFERENCE_LOCATION` join for the genuinely-duplicate columns (`inserteddatetime`, `updateddatetime`, `filename`). Client 164 is the reference for that variant.

### Greenplum source of truth

The original Greenplum versions (`secure.get_secure_json` PL/Python UDFs over `ardm_<n>.ardm_json`) are kept in repo for reference but **not** deployed by Lunar:

- [`Sources/Databases/Ardm.Secure/Legacy/get_transaction_json/`](../../../Sources/Databases/Ardm.Secure/Legacy/get_transaction_json/)

One file per client (`<client_id>.sql`); the rare client whose function body differs across GP clusters gets one file per cluster (`<client_id>.<cluster>.sql`). The folder sits outside every `Content Include` glob in `Ardm.Secure.csproj` so the SQL stays in version control without ever being installed against a database. See `Legacy/README.md` for layout and naming conventions.

When reading a GP source, watch the **constants at the top** of the function body — they're per-client feature flags that drive optional behaviour:

| Constant | Meaning |
|---|---|
| `GET_DISCOUNT_STAFF_ID` | When `True`, do a second `reference_employee` lookup using the header field named by `DISCOUNT_EMP_FIELD_NAME` and write it under the per-client output key (`DISCOUNT_EMPLOYEE_INFO`, or a hardcoded key further down). |
| `GET_ORIG_TENDER_TYPES` | When `True`, expand `recalledtransaction` and look up tender on each `origtransactionid`. |
| `DISCOUNT_EMP_FIELD_NAME` | The header column to read the staff identifier from — varies per client (`discountstaffid`, `purchasingcashierno`, etc.). |

## Transaction Vault · Snowflake fallback function — per-client overrides (cont. 2)
_chunk 593 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

| `DISCOUNT_EMPLOYEE_INFO` | The JSON output key the resolved employee is written under (some clients hardcode this further down instead). |

The generator that produced each Snowflake override's `Deviations from the standard get_secure_json that are NOT yet translated` block detects whether the *code path* exists, not whether the flag is on. Re-read the GP source before translating: if the relevant constant is `False`, the deviation can be dropped without further action.

**Always update the GP file alongside the SF override** while Greenplum is still serving any client. Once a client is fully cut over to Snowflake-only, the corresponding GP file can be deleted.

---

## Transaction Vault · Testable data mode
_chunk 594 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

For lower-environment deployment slots (`local`, `dev`, `cicd`, `qa`, `showcase`, plus `staging` for client IDs ≤ 20), the provider redirects all tenants to a pair of shared test clients:

- **ARDM V1 tenants** → client ID `7`
- **ARDM V2 tenants** → client ID `15`

This avoids uploading the same generated test data for every tenant into blob/table storage — one copy per ARDM schema version is enough since the data is identical across test tenants. Membership of the V1 set is driven by the `Clients.Ardm.SchemaV1` global config item (comma-separated client IDs).

---

## Transaction Vault · How test data gets into Table Storage
_chunk 595 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

Every morning, four Azure DevOps pipelines generate ~10k test transactions per ARDM schema version (V1 and V2) against `gp4.test.retail`, with 30-day retention:

```
Generate testable ARDM data  (Azure DevOps → Greenplum)
    ↓
Generate ardm_json            (generate_ardm_json function)
    ↓
func.export_to_blob()         (upload JSON files)
    ↓
blob_to_tablestorage          (copy into Azure Table Storage)
```

The Data API reads from Table Storage — so once the blob-to-tablestorage step runs, new transactions are queryable.

---

## Transaction Vault · Configuration
_chunk 596 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

### Global (set in Control Panel or arpfiles)

| Config item | Purpose |
|---|---|
| `DataApi.BaseUrl` | Data API base URL for the environment |
| `DataApi.Username`, `DataApi.Password` | Basic auth credentials |
| `DataApi.EnableDebug` | Toggles debug response headers |

### Per-client feature flags

| Flag | Effect |
|---|---|
| `Feature.DataApi.EnableTableStorageEventProvider` | Use the Data API for receipts (vs falling back to Greenplum entirely) |
| `Feature.DataApi.EnableBatchedEventSummariesEndpoint` | Use the batch endpoint. Not safe in prod at time of writing |
| `Feature.DataApi.EnableFallbackToGenericEventProvider` | Allow fallback to Greenplum `GenericEventProvider` (default: true) |
| `Feature.DataApi.EnableFallbackToSnowflakeEventProvider` | Allow fallback to Snowflake scalar/table functions |

### Per-client routing

| Item | Purpose |
|---|---|
| `DataApi.CutOffDate`, `DataApi.CutOffDate.Ecomm` | ISO date; before this, fall back to Greenplum |
| `DataApi.EventSummaryFields`, `DataApi.EventSummaryFields.Ecomm` | Override the default summary field list |
| `DataApi.FallbackConnectionName` | Connection name for the Greenplum fallback |
| `Snowflake.EventProvider.FallbackConnectionName` | Connection name for the Snowflake fallback (default `pos-data`) |

### Obsolete

| Flag | Status |
|---|---|
| `Feature.DataApi.EnableTableStorageEventProviderV2` | Obsolete — was for summaries rollout |
| `Feature.DataApi.EnableTestableDataMode` | Obsolete — now driven by deployment slot |

---

## Transaction Vault · Verifying in place
_chunk 597 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

From the Transaction Viewer:

1. Open DevTools → Network.
2. Drill into a transaction.
3. Look for the summaries and details requests.
4. Check the response headers — `Eventsource` tells you which provider served it, `Eventinfo` how long it took.

If you see `GenericEventProvider` when you expected `TableStorageEventProvider`, it usually means the transaction date is before `DataApi.CutOffDate` or the API returned a 404 (data not in Table Storage for that client).

---

## Transaction Vault · Key file pointers
_chunk 598 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

| Concern | File |
|---|---|
| Table-storage provider | `Sources/Core/Core/Event Providers/TableStorageEventProvider.cs` |
| Base + Greenplum fallback | `Sources/Core/Core/Event Providers/GenericEventProvider.cs` |
| Provider factory | `Sources/Core/Core/Event Providers/EventProviderFactory.cs` |
| Refit API contract | `ApprissRetail.Secure.Common.Api.IArdmJsonApi` |
| Snowflake scalar function call | `TableStorageEventProvider.GetStoreEventFromSnowflake` / `GetOrderEventFromSnowflake` |
| Event summary projection | `TableStorageEventProvider.BuildEventSummary` |

## Transaction Vault · Related
_chunk 599 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/transaction-vault.md_

- `search.md` — bulk aggregation queries against POS data (a different path)
- `../databases/snowflake.md` / `../databases/greenplum.md` — the engines that back the fallbacks
- `../data-model.md` — ARDM ingestion pipeline that ultimately feeds Table Storage
- `../observability.md` — how provider timings surface in traces/metrics

## User Data · Overview
_chunk 600 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

User Data allows users to upload CSV files that become queryable data sources in the search system. The CSV data is stored in the repo (Azure Blob Storage via arpfiles) and materialised into a JSONB table in Snowflake and Greenplum, enabling joins against other search data areas.

---

## User Data · Overview
_chunk 601 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

```
User uploads CSV via UI
    ↓
UserDataManager validates and stores 4 files in repo:
  .csv  — raw data
  .builder — search builder definition
  .searchable — searchable metadata
  .xml — format file (column types, formatting)
    ↓
UploadUserDataJob (background) materialises rows into ARDM:
  secure.UserData (Greenplum) / SECURE_USERDATA (Snowflake)
  Each row stored as { vfp, rownumber, rowdata (JSON) }
    ↓
Search system queries the JSON table via JSON path expressions
  Can join to other data areas (POS transactions, etc.)
```

---

## User Data · CSV Upload
_chunk 602 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

### UI

The UserDataManager app provides the upload interface.

**Controller:** `Sources/UI/UI/Areas/UserDataManager/Controllers/ApiController.cs`

| Endpoint | Purpose |
|---|---|
| `POST /api/v1/upload` | Upload new CSV |
| `POST /api/v1/editupload` | Replace existing CSV |
| `POST /api/v1/save` | Persist validated upload as user data |
| `POST /api/v1/update` | Update existing user data |
| `POST /api/v1/delete` | Delete user data and materialised rows |
| `GET /api/v1/download` | Download original CSV |
| `POST /api/v1/validateFile` | Validate CSV before saving |
| `GET /api/v1/getuserdata` | List user data definitions |
| `GET /api/v1/permissions` | Check user permissions |
| `GET /api/v1/getAffectedSearchNames` | Searches that reference this data |

**Permissions:** `userdatamanager.app` with `read`, `create`, `edit`, `delete` permissions.
Constants: `Sources/Core/Core/UserActivity/UserData/Constants/UserDataConstants.cs`

### Upload Flow

1. User uploads CSV file
2. File stored temporarily at `/{userId}/uploads/sngFileUpload_{guid}.csv` with `temp` tag and 30-day lifespan
3. Validation runs: header check, field type detection, data sampling
4. On save, four files are created at `/system/userdata/{userId}/{guid}`:
   - **`.csv`** — the raw CSV data
   - **`.builder`** — search builder definition (XML)
   - **`.searchable`** — searchable metadata for the search system
   - **`.xml`** — format file with column types and formatting info

### Validation

`Sources/Core/Core/UserActivity/UserData/Core/UserDataValidation/`

Supported column types:
- String
- Int64
- Decimal (with configurable thousands/decimal separators)
- Date (culture-specific parsing)
- DateTime

Configuration:
- `UserDataManager.MaxFileSizeLimitInBytes` — default 100 MB
- `UserDataManager.SampleDataLimit` — default 10 rows for validation preview
- `UserDataManager.ValidationErrorsPerColumnLimit` — default 10 errors per column

---

## User Data · Materialisation
_chunk 603 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

### JSON Row Format

Each CSV row is converted to a JSON object. Column names are transformed to camelCase:

```
"Column Name" → "columnName"   (lowercase first word, camelCase rest)
```

Conversion logic: `UserDataTypeHelper.ConvertColumnNameToJsonDocumentFormat()` in `Sources/Core/Core/UserActivity/UserData/Core/UserDataTypeHelper.cs`

### Table Schema

The same logical schema exists in both Greenplum and Snowflake:

| Column | Greenplum | Snowflake | Purpose |
|---|---|---|---|
| vfp | VARCHAR(440) | VARCHAR(440) | Builder virtual file path (PK part 1) |
| rownumber | INT | NUMBER(10,0) | Row number in CSV (PK part 2) |
| rowdata | JSONB | VARIANT | JSON document of the row data |

- **Greenplum:** GIN index on `rowdata` for JSON queries
- **Snowflake:** VARIANT type with native JSON support

**Models:**
- Greenplum: `Sources/Databases/Ardm.Secure/Models/Secure/UserData.cs`
- Snowflake: `Sources/Databases/Snowflake/` (in initial migration)

**Migration:** `Sources/Databases/Ardm.Secure/Migrations/20201123163922_Adding_UserData_Table.cs`

### Upload Job

**UploadUserDataJob** (`Sources/Core/Core/UserActivity/UserData/Jobs/UploadUserDataJob.cs`)

Runs as a background job after save:
1. Finds all builder files with extension `builder` and tag `mydata`
2. Calls stored procedure `secure.ClearUserDataByVfp` to clear existing rows for the VFP
3. Bulk inserts rows using `UserDataBulkInsertReader`
4. Targets the ARDM POS direct connection

**Bulk insert reader:** `Sources/Core/Core/UserActivity/UserData/Core/Readers/UserDataBulkInsertReader.cs` — reads CSV and emits rows as `(vfp, rownumber, rowdata)` tuples.

### Snowflake-Specific

**Bulk reader:** `Sources/Hatr/ApprissRetail.Secure.Hatr/DatabaseAccess/Implementation/Snowflake/SnowflakeUserDataBulkInsertReader.cs`

**Clear procedure:**
```sql
-- Sources/Databases/Snowflake/Programmability/.../ClearUserDataByVfp.sql
CREATE OR REPLACE PROCEDURE SECURE_CLEARUSERDATABYVFP(VFP VARCHAR)
DELETE FROM SECURE_USERDATA UD WHERE UD.VFP = :VFP;
```

**Migration activity:** `Sources/Hatr/.../MigrateToSnowflake/ImportUserDataActivity.cs` — reads all builder files and bulk inserts into Snowflake during migration.

---

## User Data · Search Integration
_chunk 604 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

User data becomes queryable through the search system by converting column references to JSON path expressions.

### PostgreSQL

`Sources/Core/Data Providers/Sql/Postgresql/Generator/Helpers/PostgresqlUserDataSearchConverter.cs`

- Sets table to `[secure].[UserData]`
- Adds mandatory condition: `vfp = {builderPath}`
- Converts display fields to JSON expression fields using `ConvertColumnNameToJsonDocumentFormat()`
- Sets `JsonPath` on expression fields for `rowdata->'field'` queries

### Search Builder

`Sources/Core/Core/UserActivity/UserData/Core/Builder/SearchBuilderDefinitionBuilder.cs`

Creates a `SearchBuilderDef` for each user data upload:
- Category: `user-data-{guid}-{modelName}`
- Builder file tagged with: `explorer mydata {name}`

`CsvSearchServiceRequestBuilder` (`Sources/Core/Core/UserActivity/UserData/Core/Builder/CsvSearchServiceRequestBuilder.cs`) builds a `SearchServiceRequest` from the CSV, adding the VFP as a condition parameter.

---

## User Data · Service Layer
_chunk 605 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

### UserDataService

`Sources/Core/Core/UserActivity/UserData/Core/UserDataService.cs` (~1700 lines)

The main service handling all CRUD operations, validation orchestration, file management, and search builder creation.

### UserDataModel

`Sources/Core/Core/UserActivity/UserData/Models/UserData.cs`

| Field | Purpose |
|---|---|
| Name | Display name |
| Description | User-provided description |
| ColumnNames | CSV column headers |
| DataTypes | Detected types per column |
| UserGroups | Permission groups with access |
| FormattingInfo | Decimal/date formatting configuration |

---

## User Data · Configuration
_chunk 606 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

| Config Item | Default | Purpose |
|---|---|---|
| `UserDataManager.UserDataAreaMaxCount` | 20 | Max user data areas per system |
| `UserDataManager.MaxFileSizeLimitInBytes` | 104857600 (100 MB) | Max upload file size |
| `UserDataManager.SampleDataLimit` | 10 | Sample rows for validation |
| `UserDataManager.ValidationErrorsPerColumnLimit` | 10 | Max validation errors shown per column |
| `UserData.CanSaveAnywayDefaultPermissionGroups` | "" | Groups allowed to save despite warnings |
| `Feature.UserData.StandardOperators` | — | Enable standard operators for queries |
| `Feature.EnableNewDependencyHandling` | — | Required for user data deletion |
| `Feature.UserData.EnableUtf8Encoding` | `false` | Makes MSSQL user-data searches decode the PSV as UTF-8 (the encoding the platform actually writes). Two pieces have to line up: (1) the OPENROWSET clause emits `CODEPAGE = '65001'`, and (2) `MsSqlFromTableWriter` publishes a UTF-8 variant of the format file (`*.Latin1_General_100_CI_AS_SC_UTF8.<ext>`) with every source `<FIELD>`'s `COLLATION` rewritten to `Latin1_General_100_CI_AS_SC_UTF8` — the per-field `COLLATION` is what SQL Server actually consults for byte→char decoding, so just adding `CODEPAGE` is not enough on its own. The variant is cached under a distinct VFP suffix, so any pre-existing cp1252 connection-specific variants remain in place. Safe to enable on Azure SQL MI; the UTF-8 collation requires SQL Server 2019+. |

---

## User Data · Related Operations
_chunk 607 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/user-data.md_

### Greenplum Migration

`Sources/Hatr/.../GpMigration/MigrateUserDataTablesActivity.cs` — executes a search for all user data definitions and re-saves them during Greenplum migration.

## Work Item Generation · Overview
_chunk 608 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Work items are flagged results from scheduled searches, automatically generated and queued for investigator review. This document covers the technical architecture of how they are created.

For product-level context, see `docs/02-products/secure.md`.

---

## Work Item Generation · Overview
_chunk 609 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Work item generation is a 3-step pipeline that runs every 15 minutes via HATR (Azure Durable Functions):

```
Step 1: Get Definition-level Requests
  Identify which work item definitions need to run for the most recently elapsed period
    ↓
Step 2: Run Definition Requests
  Execute each definition's trigger search to find matches
    ↓
Step 3: Run Deaggregation Requests
  Run deaggregation queries per row, deduplicate, insert work items
```

There are three independent generators, each with its own HATR task:

| Generator | Schedule | Purpose |
|---|---|---|
| Standard WorkItemGenerator | Every 15 min | EBR search-based work items |
| SecureAiWorkItemGenerator | Every 15 min | AI Outlier work items (see `ai-outliers.md`) |
| CashierCoachingWorkItemGenerator | Daily 11:00 AM | Cashier coaching work items |

---

## Work Item Generation · Step 1: Get Definition-level Requests
_chunk 610 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

The generator fetches expected work item definitions for the current calendar period using `WorkItemStatusService`. Each definition has a search configured to produce work items. The search MUST have a grouping. 

Before executing, a **GNG (Go/No-Go) check** verifies that prerequisite data loads are complete for each day within the period being executed. If data is still loading, the generator ignores the definnition level request and will check again the next time the work item generation task runs.

For each definition that passes GNG, a `WorkItemDefinitionGenerationRequest` record is inserted to track the execution, including the definition VFP, which period to run for, and the version of the search and work item definition (these are used to determine when we should retry after a failure).

**Key classes:**
- `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step1/WorkItemGeneratorBase.cs` — orchestrates the 3-step process
- `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step1/WorkItemGenerator.cs` — standard implementation

---

## Work Item Generation · Step 2: Run Definition Requests
_chunk 611 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Each definition's trigger search is executed against. The results identify groups of transactions that meet the search conditions.

For each matching row, a `WorkItemDeaggregationRequest` record is queued with the row's parameters. This decouples discovery from creation and allows parallel processing. It also allows us to gracefully resume deaggregation if it is interrupted without needing to rerun the definition-level search - these are sometimes very intensive.

**Parallelism:** Controlled by `MaxDegreesOfDefinitionLevelParallelism` (default: 1 definition at a time).

**Key classes:**
- `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step2/WorkItemDefinitionProcessorBase.cs`
- `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step2/Standard/WorkItemDefinitionProcessor.cs`

---

## Work Item Generation · Step 3: Run Deaggregation Requests
_chunk 612 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Each deaggregation request is processed individually:

1. Execute the deaggregation search with the row's specific parameters
2. Check for duplicates — find the work item's stack, compare transaction IDs against existing work items (see [Duplicate Detection](#duplicate-detection) below)
3. If not a duplicate, insert the work item into `workview.Workview`
4. Insert work item tags into `workview.WorkviewSubject` (work item id, tag name, tag value)
5. Insert work item teams into `workview.Teams` (work item id, team id)
6. Run analysis tiles (analysis of transactions identified in each work item + comparison between these transactions and other transactions from same store)


**Parallelism:** Controlled by `MaxDegreesOfDeaggregationParallelism` (default: 4).

**Key classes:**
- `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step3/WorkItemDeaggregationProcessor.cs`
- `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step3/WorkItem.cs` — core work item model (ID, Category, Headline, Description, LocationId, PeriodFrom/To, Priority, DueDate, PotentialValue)

---

## Work Item Generation · HATR Scheduling
_chunk 613 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Each generator is an Azure Durable Functions orchestration with a scheduled trigger and a manual trigger.

| Task | File | Task ID |
|---|---|---|
| Standard | `Sources/Hatr/.../WorkItemGenerator/WorkItemGeneratorTask.cs` | `87730dde-a246-41d1-94a4-70b2e7272bfc` |
| SecureAI | `Sources/Hatr/.../SecureAiWorkItemGenerator/SecureAiWorkItemGeneratorTask.cs` | `438c17ef-f5ec-4df4-bf79-48de7c1e2eac` |
| CashierCoaching | `Sources/Hatr/.../CashierCoachingWorkItemGenerator/CashierCoachingWorkItemGeneratorTask.cs` | `f8f61c60-ec32-4665-a4a4-d8816c5763e4` |

The standard and SecureAI generators disable the GNG check at the HATR level (`DisableGngCheck = true`) because they manage data availability checks internally.

---

## Work Item Generation · Stacked Work Items and Duplicate Detection
_chunk 614 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Work items are deduplicated using a stack hash and a transaction ID comparison.

### Stack hash (`StackHashedData`)

Identifies "the same group/result row from the same definition". Built from (pipe-delimited):

- `Category`
- `Headline`
- `SourceApp`
- All **grouping fields** from the result row (every field marked `IsGroupingField`, as `Label:Value`)

Work items sharing the same stack hash are part of the same **stack** — e.g. the same cashier at the same store from the same definition across different periods.

### How deduplication works

The stored procedure `workview.IsDuplicateWorkItem` checks two conditions (OR):

1. **Fast path** — an exact match on the **analysis result hash** (`AnalysisResultHashedData` = stack hash + period dates + event count). If an existing work item has the identical analysis result hash, it's immediately a duplicate without comparing transactions.
2. **Transaction ID comparison** — find all existing work items in the same **stack** (matching `StackHashedData`). Compare the candidate's transaction IDs against those already referenced by work items in the stack. If every transaction ID is already covered, it's a duplicate.

If neither condition is met, the candidate is not a duplicate and is inserted.

This means a work item for the same group/result row in a new period will only be created if it identifies transactions not already covered by an earlier work item in the stack.

Logic: `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Step3/WorkItem.cs` — `BuildWorkItemHashedData()` and `BuildAnalysisResultHashedData()`

---

## Work Item Generation · Database Schema
_chunk 615 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

All tables live in the `workview` schema of the Platform database.

### workview.Workview (main work items)

| Column | Type | Purpose |
|---|---|---|
| ID | BIGINT PK | Work item identifier |
| Category, Headline, Description | NVARCHAR | Display metadata from definition |
| SourceApp | NVARCHAR(200) | Source application |
| AssignedToUserID | GUID | Assigned investigator (nullable) |
| StatusID | SMALLINT | Current status |
| LocationID | BIGINT | Location scope |
| PeriodFromDateTime, PeriodToDateTime | DATE | Period covered |
| CountOfEvents | INT | Number of events identified |
| WorkItemType | NVARCHAR(64) | Type classification |
| PriorityID | SMALLINT | Priority level |
| PotentialValue | FLOAT | Estimated business value |
| CreatedDateTime | DATETIME | When generated |

Model: `Sources/Databases/Platform/Models/workview/Workview.cs`

### workview.WorkItemDefinitionGenerationRequest

Tracks each definition-level execution: RunId, definition path, period, execution times, whether deaggregation requests were created, and failure state.

Model: `Sources/Databases/Platform/Models/workview/WorkItemDefinitionGenerationRequest.cs`

### workview.WorkItemDeaggregationRequest

Tracks each row-level execution: RunId + RowId composite key, execution times, failure/duplicate/skipped flags, and a JSON representation of the parameters used for deaggregation.

Model: `Sources/Databases/Platform/Models/workview/WorkItemDeaggregationRequest.cs`

### workview.WorkItemGenerationEvent

Audit trail: RunId, RowId, WorkviewId, EventType, EventDateTime.

Model: `Sources/Databases/Platform/Models/workview/WorkItemGenerationEvent.cs`

---

## Work Item Generation · Key Stored Procedures
_chunk 616 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

| Procedure | Purpose |
|---|---|
| `workview.InsertWorkItemDefinitionGeneration` | Insert definition-level request |
| `workview.SelectIncompleteWorkItemDefinitionGenerations` | Get unfinished definition requests |
| `workview.InsertWorkItemDeaggregation` | Insert row-level deaggregation request |
| `workview.SelectIncompleteWorkItemDeaggregationRequests` | Get unfinished row requests |
| `workview.WorkviewInsert` | Insert final work item |
| `workview.WorkviewSubjectInsert` | Insert work item tags |
| `workview.AbandonWorkItemsByDefinitionRequestId` | Clean up failed batches |

---

## Work Item Generation · Configuration
_chunk 617 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

### Feature Flags

| Flag | Purpose |
|---|---|
| `WorkItemGenerator2.UseLegacyMaxWorkItemCountLogic` | Count duplicates toward max work item limit |
| `WorkItemGenerator2.UseLegacyDuplicateWorkItemCheck` | Ignore events when detecting duplicates |
| `Feature.WI2.EnableMonitorSpecificOffsets` | Use monitor-specific execution offsets |
| `Feature.WI2.PopulatePotentialValue` | Populate potential value on work items |
| `Feature.WI2.IgnoreGngCheck` | Skip data availability check |
| `Feature.WorkItemGenerator.UseAggregatedEventData` | Use aggregated vs. detailed events |
| `Feature.WorkItemGenerator.SkipWorkItemIfNoEvents` | Skip creation if no events found |

### Input Parameters

| Parameter | Default | Purpose |
|---|---|---|
| MaxDegreesOfDefinitionLevelParallelism | 1 | Parallel definitions executed |
| MaxDegreesOfDeaggregationParallelism | 4 | Parallel deaggregation requests |
| MaxDeaggregationRequestMultiplier | 1 | Queue multiplier per row |
| MinExpectedLoadCount | varies | Minimum data loads for GNG |
| TimeToWaitForExpectedLoads | varies | How long to wait for data |

Configuration: `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Models/WorkItemGeneratorInput.cs`

---

## Work Item Generation · Factory Pattern
_chunk 618 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Engineer OnB/work-item-generation.md_

Definition processors are created via factories, allowing different generators to use different processing logic:

| Factory | Processor | Used by |
|---|---|---|
| `StandardWorkItemDefinitionProcessorFactory` | `WorkItemDefinitionProcessor` | Standard generator |
| `SecureAiWorkItemDefinitionProcessorFactory` | SecureAI-specific processor | SecureAI generator |

Located in `Sources/Core/Core/Instant Analytics/WorkItemGenerator2/Models/`.
