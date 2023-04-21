<template>
    <NavBar></NavBar>

    <img src="@/assets/logo.svg" alt="Université Paris Cité" class="banner" />


    <section class="section"> <div class="container">
        <h1 class="title">Bienvenue sur le portail du projet SOC.</h1>
        <p>Le projet vise à créer un SOC (Security Operating Center) miniaturisé, commun à toute la promotion du Master 2 Cybersécurité.</p>
        <br>
        <br>
        <br>
      </div></section>
        <section class="section grp123"><div class="container">
        <h2>La promotion est séparée en cinq groupes. Les groupes ont été définis en suivant l’ordre alphabétique :</h2>
        <br>
        <div class="columns is-multiline">
  <div class="column is-one-third">
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">1er groupe</p>
      </header>
      <div class="card-content">
        <div class="content">
          L’équipe a la charge de mettre en place un SIEM grâce à QRadar et Suricata
          <ul>
            <li>QRadar : SIEM (Security Information and Event Management)</li>
            <li>Suricata : sonde de détection et de prévention d’intrusion</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="column is-one-third">
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">2ème groupe</p>
    </header>
    <div class="card-content">
      <div class="content">
        Cette équipe se charge de détecter les logs en utilisant trois outils différents :
        <ul>
          <li>
            Squid : serveur mandataire et mandataire inverse permettant de relayer les protocoles FTP, http, HTTPS, etc.
          </li>
          <li>
            Elastic : suite d’outils permettant la gestion de logs et l’analyse de données (SIEM).
          </li>
          <li>
            pfSense : système d’exploitation open source qui a pour but la mise en place de routeur et pare-feu basés sur le FreeBSD.
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>
<div class="column is-one-third">
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">3ème groupe</p>
    </header>
    <div class="card-content">
      <div class="content">
        Cette équipe, comme la précédente, s’occupe de la récupération et l’analyse de logs et de données en utilisant cette fois-ci d’autres logiciels. Ces derniers étant Snort et Splunk.
        <ul>
          <li>Snort : système de détection d'intrusion basé sur le réseau (NIDS)</li>
          <li>Splunk : plateforme d'analyse et de visualisation des données</li>
        </ul>
      </div>
    </div>
  </div>
</div>
</div>
<h3>Ces trois premiers groupes possèdent chacun leur propre outil de détection ainsi qu’un SIEM
</h3>

</div></section>
<section class="section grp56"><div class="container">
<h2 class="subtitle">Les deux derniers groupes sont chargés de la création d’un site web et de la réalisation de tests de pénétration.</h2>
<div class="columns is-multiline" >
  <div class="column is-one-third">
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">4ème groupe</p>
    </header>
    <div class="card-content">
      <div class="content">
        Cette équipe se charge des tests de pénétration et la création du site web lié au projet. Le site est codé en php et nodejs.
        <ul>
          <li>Nginx : serveur web</li>
          <li>Laravel : framework php</li>
          <li>Nodejs : framework JavaScript</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="column is-one-third">
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">5ème groupe</p>
    </header>
    <div class="card-content">
      <div class="content">
        Cette dernière équipe prend en charge la partie administration réseau (ex : serveur ntp).
        <ul>
          <li>Syslogng : serveur de collecte des logs puis les envoie vers les SIEM.</li>
          <li>Sftp : serveur de partage de fichier stockant les fichiers de configuration.</li>
          <li>Ntp : serveur de temps, le protocole ntp permet de synchroniser les horloges, les machines et tous les équipements informatiques de différents systèmes sur une référence d’heure.</li>
          <li>DNS : serveur de résolution de nom de domaine</li>
          <li>Centreon : serveur de supervision technique des équipements</li>
          <li>Dataïku : serveur de parsing des logs,</li>
          <li>OTRS : serveur fait pour envoyer des tickets, OTRS est un logiciel de relation client</li>
        </ul>
      </div>
    </div>
  </div>
</div>
</div>
</div></section>
<section class="section footer"><div class="container">
        <div class="content">
          <h2 class="subtitle">L’examen se déroulera comme suit :</h2>
          <p>
            A partir d’une machine Kali Linux, les attaquants devront attaquer ce portail en passant par des failles « délibérément laissées actives ». De l’autre côté, le SOC devra détecter cette attaque à l’aide des nombreux outils de surveillance mis en place.
          </p>
        </div>
      </div></section>
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
.grp123 {
  background-color: #74142c;
  position: relative;
  z-index: 1;
  width: 100vw; /* This will make the element take up the full width of the viewport */
  margin-left: -50vw; /* This will center the element on the page */
  left: 50%;
  color: #ffffff;
}
.grp56 {
  background-color: #ffffff;
  position: relative;
  z-index: 1;
  width: 100vw; /* This will make the element take up the full width of the viewport */
  margin-left: -50vw; /* This will center the element on the page */
  left: 50%;

}
.footer {
  background-color: #adaaaa;
  position: relative;
  z-index: 1;
  width: 100vw; /* This will make the element take up the full width of the viewport */
  margin-left: -50vw; /* This will center the element on the page */
  left: 50%;
}

</style>
