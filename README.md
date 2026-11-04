![Karim Hamdy](assets/banner.svg)

# Karim Hamdy: Backend & AI Engineering, Automation Flows, and Real-time Systems

**TL;DR:** I'm **Karim Hamdy**, a backend and AI engineer who builds with **Laravel and PHP**. I connect apps to **any AI provider** (OpenAI, Claude, Gemini, open-source and local models), design **automation flows** that run the boring parts of a business, and build **Growth AI** systems that score leads, personalise outreach and learn from results. Underneath it all are solid APIs, real-time events and location-aware data.

* **AI integrations**: One backend, any model, with fallbacks, cost tracking and clean abstractions.
* **Automation flows**: n8n, Make, Zapier, webhooks and custom Laravel pipelines.
* **Growth AI**: Lead scoring, AI-written outreach, chatbots and support triage.

* [laravel-eloquent-spatial](https://github.com/karim20160300/laravel-eloquent-spatial): Geospatial types and queries for Eloquent.
* [php-maps-fleetengine](https://github.com/karim20160300/php-maps-fleetengine): PHP access to Google Maps Fleet Engine.
* [laravel-realtime](https://github.com/karim20160300/laravel-realtime-using-redis-socket.io-and-laravel-echo): Redis, Socket.io and Laravel Echo, end to end.
* [realTime-App-With-VueJs](https://github.com/karim20160300/realTime-App-With-VueJs): A live single-page app with Pusher, JWT and Vuetify.

<p align="center">
  <img src="assets/badge-ai.svg" height="28" alt="AI Integrations" />
  <img src="assets/badge-automation.svg" height="28" alt="Automation" />
  <img src="assets/badge-growth.svg" height="28" alt="Growth AI" />
  <img src="assets/badge-laravel.svg" height="28" alt="Laravel" />
  <img src="assets/badge-realtime.svg" height="28" alt="Real-time" />
  <img src="assets/badge-spatial.svg" height="28" alt="Geospatial" />
  <img src="assets/badge-db.svg" height="28" alt="Databases" />
  <img src="assets/badge-vue.svg" height="28" alt="Vue.js" />
</p>

<p align="center">
  <a href="https://github.com/karim20160300">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=FF2D55&center=true&vCenter=true&width=640&lines=Plugging+any+AI+into+any+app.;Automating+workflows+end+to+end.;Growth+AI+that+learns+from+results.;Building+APIs+that+don%27t+flinch.;Pushing+events+in+real+time." alt="Typing intro" />
  </a>
</p>

<p align="center">
  <a href="#ai-integration-hub">AI Hub</a> ·
  <a href="#the-ai-growth-loop">Growth Loop</a> ·
  <a href="#the-request-lifecycle">Lifecycle</a> ·
  <a href="#featured-work">Featured work</a> ·
  <a href="#the-stack">Stack</a> ·
  <a href="#how-i-build">How I build</a> ·
  <a href="#github-pulse">Pulse</a> ·
  <a href="#lets-connect">Connect</a>
</p>

## AI integration hub

I treat AI models like any other service: behind a clean interface, swappable and measurable. Your app talks to one Laravel core; the core picks the right provider for the job, falls back if one fails, and tracks tokens and cost.

![AI integration hub: Laravel AI core connecting OpenAI, Anthropic Claude, Google Gemini, Mistral, DeepSeek and local LLMs to automations, CRMs, chatbots, webhooks and analytics](assets/ai-hub.svg)

## The AI growth loop

Automations get smarter when results feed back into them. Every flow I build follows this loop: something happens, AI understands it, the system decides, acts, and measures what worked.

![AI growth loop: Trigger, Enrich, Decide, Act, Measure](assets/growth-loop.svg)

## The request lifecycle

Every project I build follows the path of a single request. It gets **routed**, **validated**, **queried**, passed through **AI** when it needs to think, **located**, **broadcast**, and finally **rendered**. Each stage is a place where I like to go deep.

![The request lifecycle: Route, Validate, Query, Think, Locate, Broadcast, Render](assets/lifecycle.svg)

<p align="center"><sub>Route · Validate · Query · Think · Locate · Broadcast · Render</sub></p>

## Featured work

<table>
<tr>
<td width="50%"><a href="https://github.com/karim20160300/laravel-eloquent-spatial"><img src="assets/project-spatial.svg" width="580" alt="laravel-eloquent-spatial: spatial data types and queries for Eloquent" /></a></td>
<td width="50%"><a href="https://github.com/karim20160300/php-maps-fleetengine"><img src="assets/project-fleet.svg" width="580" alt="php-maps-fleetengine: PHP bridge to Google Maps Fleet Engine" /></a></td>
</tr>
<tr>
<td><a href="https://github.com/karim20160300/laravel-realtime-using-redis-socket.io-and-laravel-echo"><img src="assets/project-realtime.svg" width="580" alt="Laravel real-time with Redis, Socket.io and Laravel Echo" /></a></td>
<td><a href="https://github.com/karim20160300/realTime-App-With-VueJs"><img src="assets/project-vue.svg" width="580" alt="Real-time Vue app with Pusher, JWT and Vuetify" /></a></td>
</tr>
<tr>
<td><a href="https://github.com/karim20160300/LaravelValidationRulesWithParamerrsOrLogic"><img src="assets/project-validation.svg" width="580" alt="Laravel validation rules with constructor parameters" /></a></td>
<td><a href="https://github.com/karim20160300/laravel-db-features"><img src="assets/project-db.svg" width="580" alt="Laravel database features: Eloquent and the query builder" /></a></td>
</tr>
</table>

## The stack

| Layer | What I use | Why it matters |
| :--- | :--- | :--- |
| **AI providers** | OpenAI, Anthropic Claude, Google Gemini, Mistral, DeepSeek, Ollama | The right model for each task, with fallbacks |
| **AI engineering** | Prompt design, function calling, RAG, embeddings, agents | AI that uses your data and takes real actions |
| **Automation** | n8n, Make, Zapier, webhooks, Laravel queues | Workflows that run the business while you sleep |
| **Growth AI** | Lead scoring, AI outreach, chatbots, CRM sync | More leads handled with less manual work |
| **API** | Laravel, PHP, REST, JWT | Clean, versioned endpoints with real auth |
| **Data** | MySQL, Eloquent, Query Builder | Fast queries and models that read like English |
| **Location** | Spatial columns, Google Maps, Fleet Engine | Distance, geofencing and live vehicle tracking |
| **Real-time** | Redis, Socket.io, Laravel Echo, Pusher | Events that reach users the moment they happen |
| **Frontend** | Vue.js, Vuetify, TypeScript | Enough UI to ship the whole feature myself |
| **Foundations** | Java, ASP.NET, Linux, OS concepts | Scheduling, file systems and how machines think |

<p align="center">
  <img src="https://img.shields.io/badge/OpenAI-0b0f1a?style=for-the-badge&logo=openai&logoColor=e6edf3" alt="OpenAI" />
  <img src="https://img.shields.io/badge/Claude-0b0f1a?style=for-the-badge&logo=anthropic&logoColor=ff7a59" alt="Claude" />
  <img src="https://img.shields.io/badge/Gemini-0b0f1a?style=for-the-badge&logo=googlegemini&logoColor=4cc9f0" alt="Gemini" />
  <img src="https://img.shields.io/badge/Ollama-0b0f1a?style=for-the-badge&logo=ollama&logoColor=e6edf3" alt="Ollama" />
  <img src="https://img.shields.io/badge/n8n-0b0f1a?style=for-the-badge&logo=n8n&logoColor=ff2d55" alt="n8n" />
  <img src="https://img.shields.io/badge/Make-0b0f1a?style=for-the-badge&logo=make&logoColor=a78bfa" alt="Make" />
  <img src="https://img.shields.io/badge/Zapier-0b0f1a?style=for-the-badge&logo=zapier&logoColor=ff7a59" alt="Zapier" />
  <img src="https://img.shields.io/badge/LangChain-0b0f1a?style=for-the-badge&logo=langchain&logoColor=42d392" alt="LangChain" />
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=php,laravel,py,mysql,redis,vue,ts,js,java,linux,git,docker,postman&perline=13" alt="Tech stack icons" />
</p>

## How I build

<details>
<summary><strong>Any AI provider, one interface</strong></summary>

> [!TIP]
> The app should never care which model answered. Providers change; the interface doesn't.

```php
$reply = AI::using(config('ai.default'))      // openai, claude, gemini, ollama...
    ->fallback(['claude', 'gemini'])
    ->system('You are a sales assistant. Answer in JSON.')
    ->prompt($lead->message)
    ->json();

$lead->update(['score' => $reply['score'], 'intent' => $reply['intent']]);
```
</details>

<details>
<summary><strong>Automations that call AI, then act</strong></summary>

```php
// A new lead arrives from a form, WhatsApp or a webhook
Event::listen(LeadCreated::class, function ($e) {
    Pipeline::send($e->lead)
        ->through([EnrichWithAI::class, ScoreLead::class, SyncToCrm::class, SendFollowUp::class])
        ->thenReturn();
});
```
</details>

<details>
<summary><strong>Validation is a design tool, not an afterthought</strong></summary>

> [!TIP]
> Rules that take constructor parameters turn validation into reusable building blocks.

```php
$request->validate([
    'pickup' => ['required', new WithinServiceArea($city)],
    'seats'  => ['required', new AvailableSeats($trip)],
]);
```
</details>

<details>
<summary><strong>Location should be a first-class query</strong></summary>

```php
// Drivers within 5 km of the customer, nearest first
Driver::query()
    ->whereDistanceSphere('location', $customer->location, '<', 5000)
    ->orderByDistanceSphere('location', $customer->location)
    ->get();
```
</details>

<details>
<summary><strong>If it changed, the user should already know</strong></summary>

```php
// Server
broadcast(new TripUpdated($trip))->toOthers();
```
```js
// Client
Echo.private(`trips.${tripId}`).listen('TripUpdated', e => updateMap(e.trip));
```
</details>

## GitHub pulse

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=karim20160300&show_icons=true&hide_border=true&bg_color=0b0f1a&title_color=ff2d55&icon_color=42d392&text_color=e6edf3" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=karim20160300&layout=compact&hide_border=true&bg_color=0b0f1a&title_color=ff2d55&text_color=e6edf3" alt="Top languages" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=karim20160300&bg_color=0b0f1a&color=e6edf3&line=ff2d55&point=42d392&area=true&hide_border=true" alt="Contribution graph" />
</p>

## Let's connect

<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0b0f1a?style=for-the-badge&logo=linkedin&logoColor=42d392" alt="LinkedIn" /></a>
  <a href="mailto:YOUR-EMAIL"><img src="https://img.shields.io/badge/Email-0b0f1a?style=for-the-badge&logo=gmail&logoColor=ff2d55" alt="Email" /></a>
  <a href="https://github.com/karim20160300?tab=repositories"><img src="https://img.shields.io/badge/All_Repos-0b0f1a?style=for-the-badge&logo=github&logoColor=e6edf3" alt="Repositories" /></a>
</p>

<p align="center"><sub>Open to AI integration, automation and backend projects. If it can be automated, made smarter or updated live, I'm interested.</sub></p>
