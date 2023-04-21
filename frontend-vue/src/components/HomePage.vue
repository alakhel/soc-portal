<template>
  <div>
    <NavBar></NavBar>

    <img src="@/assets/logo.svg" alt="Université Paris Cité" class="banner" />

    <section class="section">
      <div class="container">
        <h1 class="title">Bienvenue sur le portail du projet SOC.</h1>
        <p>Le projet vise à créer un SOC (Security Operating Center) miniaturisé, commun à toute la promotion du Master 2 Cybersécurité.</p>

        <div class="content">
          <h2 class="subtitle">La promotion est séparée en cinq groupes. Les groupes ont été définis en suivant l’ordre alphabétique :</h2>
          <ul>
            <li>
              <strong>1er groupe :</strong> L’équipe a la charge de mettre en place un SIEM grâce à QRadar et Suricata
              <ul>
                <li>QRadar : SIEM (Security Information and Event Management)</li>
                <li>Suricata : sonde de détection et de prévention d’intrusion</li>
              </ul>
            </li>
            ...
          </ul>
        </div>

        <div class="content">
          <h2 class="subtitle">L’examen se déroulera comme suit :</h2>
          <p>
            A partir d’une machine Kali Linux, les attaquants devront attaquer ce portail en passant par des failles « délibérément laissées actives ». De l’autre côté, le SOC devra détecter cette attaque à l’aide des nombreux outils de surveillance mis en place.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';

export default {
  components: {
    NavBar,
  },
};
</script>

<style>
.banner {
  width: 100%;
  height: 100%;
}
</style>
