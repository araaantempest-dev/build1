
<section class="section" style="padding-top:0" id="ambiance"><div class="ambiance-grid">
<div class="ambiance-card" data-rl><div class="ambiance-bg">&#127863;</div><h3>The Wine <em>Cellar</em></h3><p>Walk through our temperature-controlled cellar housing 2,400 labels. Your sommelier will guide you through regions, vintages, and the stories behind each bottle.</p></div>
<div class="ambiance-card" data-rr><div class="ambiance-bg">&#128092;</div><h3>Private <em>Dining</em> Rooms</h3><p>Three secluded private rooms seating 6 to 24 guests, available for celebrations, corporate dinners, and proposals. Each room carries its own bespoke menu.</p></div>
<div class="ambiance-card" data-rl style="--rd:100ms"><div class="ambiance-bg">&#127817;</div><h3>The Open <em>Kitchen</em></h3><p>Our main dining room faces a full glass wall overlooking the kitchen &mdash; watch the ballet of 22 chefs working in silence and precision as your meal is composed live.</p></div>
<div class="ambiance-card" data-rr style="--rd:100ms"><div class="ambiance-bg">&#127800;</div><h3>Garden <em>Terrace</em></h3><p>Open May through October &mdash; alfresco dining where live herbs and edible flowers grow alongside your table, and candles light the evening into midnight.</p></div>
</div></section>
<section class="cta-section" id="reservations">
<p class="cta-label" data-reveal>Reserve Your Seat</p>
<h2 class="cta-title" data-reveal style="--rd:80ms">Begin an Evening<br>You Will <em>Never Forget</em></h2>
<p class="cta-body" data-reveal style="--rd:180ms">Tables are limited to 34 covers per evening. We recommend reserving at least 3 weeks in advance. Dietary requirements, occasion notes, and wine preferences are welcomed at booking.</p>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap" data-reveal style="--rd:260ms"><button class="btn-gold" style="font-size:12px;padding:18px 52px">Reserve a Table</button><button class="btn-ghost" style="font-size:12px;padding:17px 48px">Enquire for Private Dining</button></div>
<p class="cta-note" data-reveal style="--rd:340ms">Dress code: <em>Smart Elegant</em> &bull; Arrival: 30 min prior recommended &bull; Duration: Approx. 3.5 hrs</p>
</section>
<div class="footer-wrap"><footer>
<div><div class="footer-name">Lumiere</div><p class="footer-desc">The fine dining destination for those who believe every meal should be a masterpiece of art, craft, and memory.</p><div class="footer-hours">Tue &ndash; Sat &bull; 18:30 &ndash; 23:00<br>Sunday Brunch &bull; 11:00 &ndash; 15:00<br>Closed Monday</div></div>
<div class="footer-col"><h5 class="footer-col-title">Dining</h5><ul><li><a href="#menu">Tasting Menu</a></li><li><a href="#menu">A La Carte</a></li><li><a href="#ambiance">Chef's Table</a></li><li><a href="#ambiance">Wine Cellar</a></li></ul></div>
<div class="footer-col"><h5 class="footer-col-title">Visit</h5><ul><li><a href="#">Reservations</a></li><li><a href="#ambiance">Private Events</a></li><li><a href="#">Gift Vouchers</a></li><li><a href="#">Dress Code</a></li></ul></div>
<div class="footer-col"><h5 class="footer-col-title">About</h5><ul><li><a href="#">The Chefs</a></li><li><a href="#">Our Story</a></li><li><a href="#">Press &amp; Awards</a></li><li><a href="#">Careers</a></li></ul></div>
<div class="footer-bottom"><span class="footer-copy">&copy; <span id="yr"></span> Lumiere Fine Dining. All rights reserved.</span><div class="footer-social"><a href="#">Instagram</a><a href="#">Facebook</a><a href="#">TripAdvisor</a></div></div>
</footer></div>
</div>
<script type="module">

import * as THREE from 'three';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js';
import { GammaCorrectionShader } from 'three/examples/jsm/shaders/GammaCorrectionShader.js';
import { CopyShader } from 'three/examples/jsm/shaders/CopyShader.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import Lenis from 'https://unpkg.com/lenis@1.3.23/dist/lenis.mjs';

document.getElementById('yr').textContent = new Date().getFullYear();
const PRM = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

const CONFIG = {
  rimColor:'#c1faff', rimPower:2.4, nightLights:10, terrainDepth:0.33, terrainShade:1.3,
  oceanGlint:0.45, oceanDeep:0.12, oceanFlow:3, oceanFlowSpeed:0.8, oceanFlowScale:2.1,
  glowColor:'#3a6cff', glowIntensity:3.35, planetRadius:1.95, spin:0.03, initRotation:2.07,
  tilt:0.37, autoRotate:0,
  cloud1Height:1.005, cloud1Opacity:0.6, cloud1Spin:0.06,
  cloud2Height:1.03,  cloud2Opacity:0.5, cloud2Spin:0.14,
  cloud3Height:1.075, cloud3Opacity:0.5, cloud3Spin:0.1,
  bgColor:'#040a1e', flameColor:'#3a6cff', flameColor2:'#c1faff', flameAmt:0.15,
  atmoColor:'#9fc4ff', atmoCount:320, atmoSize:22, atmoSpeed:0.8,
  starColor:'#cfe0ff', starCount:1400, starSize:1.6, starFlicker:1,
  markerColor:'#ffd27a', markerCount:60, markerSize:16, markerSpeed:0.5,
};
const LAYERS = { NONE:0, TORUS_SCENE:1, BLOOM_SCENE:2, ENTIRE_SCENE:3 };
const ASSET = 'https://api.getlayers.ai/storage/v1/object/public/public/assets/ascend-d9857ad1f2';

const Lerp = (a,b,t) => a+(b-a)*t;
const clampV = (v,lo,hi) => Math.max(lo,Math.min(hi,v));
function hexToVec3(hex){
  const r=parseInt(hex.slice(1,3),16)/255, g=parseInt(hex.slice(3,5),16)/255, b=parseInt(hex.slice(5,7),16)/255;
  return new THREE.Vector3(r,g,b);
}
function smoothstepF(t){ return t*t*(3-2*t); }
function sample(stops,p){
  for(let i=0;i<stops.length-1;i++){
    const a=stops[i], b=stops[i+1];
    if(p>=a.p && p<=b.p){ const t=(p-a.p)/(b.p-a.p); return Lerp(a.v,b.v,smoothstepF(t)); }
  }
  return stops[stops.length-1].v;
}

const SNOISE = `
vec4 permute(vec4 x){return mod(((x*34.0)+1.0)*x,289.0);}
vec4 taylorInvSqrt(vec4 r){return 1.79284291400159-0.85373472095314*r;}
float snoise(vec3 v){
  const vec2 C=vec2(1.0/6.0,1.0/3.0);const vec4 D=vec4(0.0,0.5,1.0,2.0);
  vec3 i=floor(v+dot(v,C.yyy));vec3 x0=v-i+dot(i,C.xxx);
  vec3 g=step(x0.yzx,x0.xyz);vec3 l=1.0-g;
  vec3 i1=min(g.xyz,l.zxy);vec3 i2=max(g.xyz,l.zxy);
  vec3 x1=x0-i1+1.0*C.xxx;vec3 x2=x0-i2+2.0*C.xxx;vec3 x3=x0-1.0+3.0*C.xxx;
  i=mod(i,289.0);
  vec4 p=permute(permute(permute(i.z+vec4(0.0,i1.z,i2.z,1.0))+i.y+vec4(0.0,i1.y,i2.y,1.0))+i.x+vec4(0.0,i1.x,i2.x,1.0));
  float n_=1.0/7.0;vec3 ns=n_*D.wyz-D.xzx;
  vec4 j=p-49.0*floor(p*ns.z*ns.z);
  vec4 x_=floor(j*ns.z);vec4 y_=floor(j-7.0*x_);
  vec4 x=x_*ns.x+ns.yyyy;vec4 y=y_*ns.x+ns.yyyy;vec4 h=1.0-abs(x)-abs(y);
  vec4 b0=vec4(x.xy,y.xy);vec4 b1=vec4(x.zw,y.zw);
  vec4 s0=floor(b0)*2.0+1.0;vec4 s1=floor(b1)*2.0+1.0;vec4 sh=-step(h,vec4(0.0));
  vec4 a0=b0.xzyw+s0.xzyw*sh.xxyy;vec4 a1=b1.xzyw+s1.xzyw*sh.zzww;
  vec3 p0=vec3(a0.xy,h.x);vec3 p1=vec3(a0.zw,h.y);vec3 p2=vec3(a1.xy,h.z);vec3 p3=vec3(a1.zw,h.w);
  vec4 norm=taylorInvSqrt(vec4(dot(p0,p0),dot(p1,p1),dot(p2,p2),dot(p3,p3)));
  p0*=norm.x;p1*=norm.y;p2*=norm.z;p3*=norm.w;
  vec4 m=max(0.5-vec4(dot(x0,x0),dot(x1,x1),dot(x2,x2),dot(x3,x3)),0.0);m=m*m;
  return 42.0*dot(m*m,vec4(dot(p0,x0),dot(p1,x1),dot(p2,x2),dot(p3,x3)));
}`;

const canvas = document.getElementById('planetCanvas');
let W = window.innerWidth, H = window.innerHeight;

const renderer = new THREE.WebGL1Renderer({canvas, antialias:true});
renderer.setPixelRatio(devicePixelRatio);
renderer.setSize(W,H);
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.VSMShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000);

const camera = new THREE.PerspectiveCamera(40, W/H, 0.1, 200);
camera.position.set(0,0,8);
camera.layers.enable(LAYERS.TORUS_SCENE);
camera.layers.enable(LAYERS.BLOOM_SCENE);
camera.layers.enable(LAYERS.ENTIRE_SCENE);
scene.add(camera);

const ambLight = new THREE.AmbientLight(0xffffff,1.8);
ambLight.layers.set(LAYERS.ENTIRE_SCENE);
scene.add(ambLight);
const dirLight = new THREE.DirectionalLight(0xffffff,0.8);
dirLight.position.set(0,10,2);
dirLight.layers.set(LAYERS.ENTIRE_SCENE);
scene.add(dirLight);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; controls.dampingFactor = 0.06;
controls.enablePan = false; controls.enabled = false;
controls.autoRotate = true; controls.autoRotateSpeed = CONFIG.autoRotate;
controls.minDistance = 3.5; controls.maxDistance = 16;
controls.target.set(0,0,0);

const FinalPass = {
  uniforms:{
    iTime:{value:0}, tDiffuse:{value:null}, torusTexture:{value:null},
    bloomTexture:{value:null}, haloTexture:{value:null},
    uBg:{value:hexToVec3(CONFIG.bgColor)},
    uFlameA:{value:hexToVec3(CONFIG.flameColor)},
    uFlameB:{value:hexToVec3(CONFIG.flameColor2)},
    uFlameAmt:{value:CONFIG.flameAmt},
  },
  vertexShader:`varying vec2 vUv;void main(){vUv=uv;gl_Position=vec4(position,1.0);}`,
  fragmentShader:`
    uniform float iTime;
    uniform sampler2D tDiffuse,bloomTexture,torusTexture,haloTexture;
    uniform vec3 uBg,uFlameA,uFlameB;
    uniform float uFlameAmt;
    varying vec2 vUv;
    vec3 warp3d(vec3 pos,float t){
      float curv=.8,a=1.9,b=0.7;pos*=2.;
      pos.x+=curv*sin(t+a*pos.y)+t*b;pos.y+=curv*cos(t+a*pos.x);
      pos.y+=curv*sin(t+a*pos.z)+t*b;pos.z+=curv*cos(t+a*pos.y);
      pos.z+=curv*sin(t+a*pos.x)+t*b;pos.x+=curv*cos(t+a*pos.z);
      return 0.5+0.5*cos(pos.xyz+vec3(1,2,4));
    }
    void main(){
      vec2 uv=2.*vUv-1.;
      vec3 w=pow(warp3d(vec3(uv.x,sin(uv.y),uv.y),iTime*1.5),vec3(1.5));
      vec3 flame=1.5*uFlameA*w.x;flame*=w.y;flame+=uFlameB*w.z;
      flame*=smoothstep(0.25,1.,abs(uv.y));
      float md=smoothstep(-0.7,1.,-uv.y*uv.x);flame*=md*md;
      vec3 bg=uBg*(1.0-0.4*length(uv));
      vec3 halo=texture2D(haloTexture,vUv).xyz;
      gl_FragColor=vec4(bg+flame*uFlameAmt+texture2D(bloomTexture,vUv).xyz+texture2D(torusTexture,vUv).xyz+texture2D(tDiffuse,vUv).xyz+halo,1.);
    }`,
};

const haloRT = new THREE.WebGLRenderTarget(W,H);

const torusComposer = new EffectComposer(renderer);
torusComposer.renderToScreen = false;
torusComposer.addPass(new RenderPass(scene,camera));
torusComposer.addPass(new ShaderPass(GammaCorrectionShader));
torusComposer.addPass(new UnrealBloomPass(new THREE.Vector2(W,H),0.22,0.2,0));
torusComposer.addPass(new ShaderPass(CopyShader));

const bloomComposer = new EffectComposer(renderer);
bloomComposer.renderToScreen = false;
bloomComposer.addPass(new RenderPass(scene,camera));
bloomComposer.addPass(new UnrealBloomPass(new THREE.Vector2(W,H),0.5,0.6,0));
bloomComposer.addPass(new ShaderPass(GammaCorrectionShader));

const finalPass = new ShaderPass(FinalPass);
finalPass.uniforms.haloTexture.value = haloRT.texture;
const finalComposer = new EffectComposer(renderer);
finalComposer.addPass(new RenderPass(scene,camera));
finalComposer.addPass(finalPass);

const STOPS_X=[{p:0,v:0},{p:0.32,v:-3.1},{p:0.64,v:3.2},{p:1,v:0}];
const STOPS_Y=[{p:0,v:-4.5},{p:0.32,v:0.55},{p:0.64,v:0.45},{p:1,v:0.15}];
const STOPS_S=[{p:0,v:2.15},{p:0.32,v:1.0},{p:0.64,v:0.92},{p:1,v:1.12}];

const worldGroup = new THREE.Group();
worldGroup.position.set(STOPS_X[0].v, STOPS_Y[0].v, 0);
worldGroup.scale.setScalar(STOPS_S[0].v);
scene.add(worldGroup);

const planetGroup = new THREE.Group();
planetGroup.rotation.z = CONFIG.tilt;
worldGroup.add(planetGroup);

const cloudGroup = new THREE.Group();
cloudGroup.rotation.z = CONFIG.tilt;
cloudGroup.visible = false;
worldGroup.add(cloudGroup);

const glowMat = new THREE.ShaderMaterial({
  transparent:true, side:THREE.DoubleSide, depthWrite:false, blending:THREE.AdditiveBlending,
  uniforms:{uGlow:{value:hexToVec3(CONFIG.glowColor)},uIntensity:{value:CONFIG.glowIntensity}},
  vertexShader:`varying vec2 vUv;void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}`,
  fragmentShader:`uniform vec3 uGlow;uniform float uIntensity;varying vec2 vUv;
    void main(){float d=length(vUv-0.5)*2.0;float a=pow(clamp(1.0-d,0.0,1.0),2.2);gl_FragColor=vec4(uGlow*a*uIntensity,a);}`,
});
const glowMesh = new THREE.Mesh(new THREE.PlaneGeometry(2,2), glowMat);
glowMesh.scale.setScalar(CONFIG.planetRadius*2.3);
worldGroup.add(glowMesh);

let planetTime=0, cloudTime=0, starTime=0, markerTime=0;

function injectPlanetShader(mat, nightTex){
  mat.onBeforeCompile = shader => {
    shader.uniforms.time = {value:planetTime};
    shader.uniforms.noiseScale = {value:30};
    shader.uniforms.speedX = {value:1.5};
    shader.uniforms.speedY = {value:2.0};
    shader.uniforms.speedZ = {value:2.5};
    shader.uniforms.rimColor = {value:hexToVec3(CONFIG.rimColor)};
    shader.uniforms.rimPower = {value:CONFIG.rimPower};
    shader.uniforms.nightBlendTexture = {value:nightTex};
    shader.uniforms.nightLights = {value:CONFIG.nightLights};
    shader.uniforms.terrainDepth = {value:CONFIG.terrainDepth};
    shader.uniforms.terrainShade = {value:CONFIG.terrainShade};
    shader.uniforms.oceanGlint = {value:CONFIG.oceanGlint};
    shader.uniforms.oceanDeep = {value:CONFIG.oceanDeep};
    shader.uniforms.oceanFlow = {value:CONFIG.oceanFlow};
    shader.uniforms.oceanFlowSpeed = {value:CONFIG.oceanFlowSpeed};
    shader.uniforms.oceanFlowScale = {value:CONFIG.oceanFlowScale};
    mat._shaderRef = shader;
    shader.vertexShader = 'varying vec2 vCustomUv;\n' + shader.vertexShader.replace('void main(){','void main(){\nvCustomUv=uv;');
    const ub = `uniform float time,noiseScale,speedX,speedY,speedZ,rimPower,nightLights,terrainDepth,terrainShade,oceanGlint,oceanDeep,oceanFlow,oceanFlowSpeed,oceanFlowScale;
      uniform vec3 rimColor;uniform sampler2D nightBlendTexture;varying vec2 vCustomUv;${SNOISE}`;
    shader.fragmentShader = ub + shader.fragmentShader;
    shader.fragmentShader = shader.fragmentShader.replace('#include <dithering_fragment>',`
      #include <dithering_fragment>
      vec3 normalizedNormal=normalize(vNormal);
      vec3 viewDir=normalize(vViewPosition);
      float rim=1.0-max(dot(viewDir,normalizedNormal),0.0);
      rim=pow(rim,rimPower);rim=pow(rim,1.5);rim*=0.7;
      vec3 currentColor=gl_FragColor.rgb;
      float blueDom=currentColor.b-max(currentColor.r,currentColor.g);
      float waterMask=clamp(smoothstep(-0.005,0.03,blueDom),0.0,1.0);
      float shimmer=snoise(vec3(vCustomUv.x*noiseScale+time*speedX,vCustomUv.y*noiseScale-time*speedY,time*speedZ));
      gl_FragColor.rgb+=waterMask*shimmer*0.025;
      float fT=time*oceanFlowSpeed*4.0;
      float fS=4.0*oceanFlowScale;
      float warp=snoise(vec3(vCustomUv.x*fS-fT*0.5,vCustomUv.y*fS+fT*0.4,fT*0.5));
      float flow=snoise(vec3(vCustomUv.x*fS*2.0+fT*0.6+warp,vCustomUv.y*fS*2.0-fT*0.5,fT*0.7));
      flow=warp*0.6+flow*0.4;
      gl_FragColor.rgb+=waterMask*flow*0.12*oceanFlow;
      gl_FragColor.rgb=mix(gl_FragColor.rgb,vec3(0.01,0.06,0.16),waterMask*oceanDeep);
      vec3 finalColor=mix(gl_FragColor.rgb,rimColor,rim);
      gl_FragColor=vec4(finalColor,1.0);
      vec3 surfPos=-vViewPosition;
      float terrH=dot(texture2D(map,vCustomUv).rgb,vec3(0.299,0.587,0.114));
      vec3 sigX=dFdx(surfPos),sigY=dFdy(surfPos);
      vec3 vR1=cross(sigY,normalizedNormal),vR2=cross(normalizedNormal,sigX);
      float fDet=dot(sigX,vR1);
      vec3 vGrad=sign(fDet)*(dFdx(terrH)*vR1+dFdy(terrH)*vR2);
      vec3 bumpedNormal=normalize(abs(fDet)*normalizedNormal-terrainDepth*vGrad);
      vec3 shadeNormal=mix(bumpedNormal,normalizedNormal,waterMask);
      vec3 cityLights=texture2D(nightBlendTexture,vCustomUv).rgb*gl_FragColor.rgb*nightLights;
      vec3 viewSunDir=normalize(vec3(-0.9,0.18,0.4));
      float ndl=dot(normalizedNormal,viewSunDir);
      float dayAmt=smoothstep(-0.05,0.35,ndl);
      float relief=dot(shadeNormal,viewSunDir)-ndl;
      gl_FragColor.rgb*=clamp(1.0+relief*terrainShade*dayAmt,0.55,1.6);
      float nightFactor=smoothstep(0.18,-0.30,ndl);
      float lightsFactor=smoothstep(0.30,-0.35,ndl);
      gl_FragColor.rgb=mix(gl_FragColor.rgb,gl_FragColor.rgb*0.08,nightFactor);
      gl_FragColor.rgb+=cityLights*lightsFactor;
      vec3 halfDir=normalize(viewSunDir+viewDir);
      float ripple=snoise(vec3(vCustomUv*240.0,time*4.0));
      float ndh=max(dot(normalizedNormal,halfDir)+ripple*0.02,0.0);
      float glint=pow(ndh,140.0);
      gl_FragColor.rgb+=glint*waterMask*dayAmt*oceanGlint*vec3(1.0,0.97,0.88);
    `);
  };
}

const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath('https://www.gstatic.com/draco/versioned/decoders/1.5.5/');
const gltfLoader = new GLTFLoader();
gltfLoader.setDRACOLoader(dracoLoader);
const texLoader = new THREE.TextureLoader();

let planetMesh=null, nightTex=null;

function findMesh(o){if(o.isMesh)return o;for(const c of o.children){const r=findMesh(c);if(r)return r;}return null;}

gltfLoader.load(ASSET+'/planet-lights.glb', gltf=>{
  const m = findMesh(gltf.scene);
  nightTex = m&&m.material&&m.material.map ? m.material.map : new THREE.Texture();
  loadPlanet();
}, undefined, ()=>{ nightTex = new THREE.Texture(); loadPlanet(); });

function loadPlanet(){
  gltfLoader.load(ASSET+'/planet.glb', gltf=>{
    const mesh = findMesh(gltf.scene);
    if(!mesh) return;
    mesh.geometry.computeBoundingSphere();
    const r = mesh.geometry.boundingSphere.radius;
    mesh.scale.setScalar(CONFIG.planetRadius/r);
    const mat = mesh.material.clone();
    mat.metalness=0; mat.roughness=1; mat.envMapIntensity=0;
    injectPlanetShader(mat, nightTex);
    mesh.material = mat;
    mesh.layers.set(LAYERS.ENTIRE_SCENE);
    planetGroup.add(mesh);
    planetMesh = mesh;
    loadClouds(mesh);
    startEntrance();
  }, undefined, e=>console.warn('planet err',e));
}

function loadClouds(pMesh){
  const defs=[
    {h:CONFIG.cloud1Height,o:CONFIG.cloud1Opacity,s:CONFIG.cloud1Spin,ry:0.0,phase:0.0},
    {h:CONFIG.cloud2Height,o:CONFIG.cloud2Opacity,s:CONFIG.cloud2Spin,ry:2.2,phase:13.0},
    {h:CONFIG.cloud3Height,o:CONFIG.cloud3Opacity,s:CONFIG.cloud3Spin,ry:4.3,phase:27.0},
  ];
  texLoader.load(ASSET+'/planet-clouds.png', tex=>{
    tex.wrapS=tex.wrapT=THREE.RepeatWrapping;
    tex.repeat.set(5,5);
    defs.forEach(def=>{
      const geo = new THREE.SphereGeometry(CONFIG.planetRadius*def.h,64,64);
      const mat = new THREE.MeshStandardMaterial({map:tex,transparent:true,depthWrite:false});
      mat._cloudSpin = def.s;
      mat.onBeforeCompile = shader=>{
        shader.uniforms.uTime={value:cloudTime};
        shader.uniforms.noiseScale={value:20};
        shader.uniforms.uSpeedX={value:1};
        shader.uniforms.uSpeedY={value:2};
        shader.uniforms.uSpeedZ={value:2};
        shader.uniforms.uOpacity={value:def.o};
        shader.uniforms.uPhase={value:def.phase};
        mat._cloudShaderRef = shader;
        shader.vertexShader='varying vec2 vCloudUv;\n'+shader.vertexShader.replace('void main(){','void main(){\nvCloudUv=uv;');
        shader.fragmentShader=`uniform float uTime,noiseScale,uSpeedX,uSpeedY,uSpeedZ,uOpacity,uPhase;varying vec2 vCloudUv;\n${SNOISE}\n`+shader.fragmentShader;
        shader.fragmentShader=shader.fragmentShader.replace('#include <dithering_fragment>',`
          #include <dithering_fragment>
          gl_FragColor.rgb=vec3(1.0);
          float cloudNoise=snoise(vec3(vCloudUv.x*noiseScale+uTime*uSpeedX+uPhase,vCloudUv.y*noiseScale-uTime*uSpeedY+uPhase,uTime*uSpeedZ+uPhase));
          float cloudNdv=max(dot(normalize(vNormal),normalize(vViewPosition)),0.0);
          float cloudEdge=pow(1.0-cloudNdv,3.0);
          float cloudMod=mix(cloudNoise,1.0,cloudEdge);
          float cloudNdl=dot(normalize(vNormal),normalize(vec3(-0.9,0.18,0.4)));
          float cloudDay=1.0-smoothstep(0.30,-0.30,cloudNdl)*0.9;
          gl_FragColor.a*=cloudMod*uOpacity*cloudDay;
        `);
      };
      const cMesh = new THREE.Mesh(geo,mat);
      cMesh.rotation.y=def.ry; cMesh.renderOrder=2;
      cMesh.layers.set(LAYERS.ENTIRE_SCENE);
      cloudGroup.add(cMesh);
    });
    cloudGroup.visible=true;
  });
}

(function buildStars(){
  const N=CONFIG.starCount;
  const pos=new Float32Array(N*3),seeds=new Float32Array(N),brights=new Float32Array(N);
  for(let i=0;i<N;i++){
    const th=Math.acos(2*Math.random()-1),ph=Math.random()*Math.PI*2,r=90;
    pos[i*3]=r*Math.sin(th)*Math.cos(ph);
    pos[i*3+1]=r*Math.sin(th)*Math.sin(ph);
    pos[i*3+2]=r*Math.cos(th);
    seeds[i]=Math.random()*100;
    brights[i]=0.35+Math.random()*0.65;
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('seed',new THREE.BufferAttribute(seeds,1));
  geo.setAttribute('bright',new THREE.BufferAttribute(brights,1));
  const mat=new THREE.ShaderMaterial({
    blending:THREE.AdditiveBlending,depthWrite:false,transparent:true,frustumCulled:false,
    uniforms:{uTime:{value:0},uSize:{value:CONFIG.starSize},uFlicker:{value:CONFIG.starFlicker},uColor:{value:hexToVec3(CONFIG.starColor)},uRes:{value:new THREE.Vector2(W,H)}},
    vertexShader:`attribute float seed;attribute float bright;uniform float uTime,uSize,uFlicker;uniform vec2 uRes;varying float vTw;
      void main(){vec4 mv=modelViewMatrix*vec4(position,1.0);float tw=0.6+0.4*sin(uTime*uFlicker+seed);vTw=bright*tw;
        gl_PointSize=max(uSize*uRes.y/900.0*(90.0/max(-mv.z,1.0)),1.0);gl_Position=projectionMatrix*mv;}`,
    fragmentShader:`uniform vec3 uColor;varying float vTw;
      void main(){vec2 p=gl_PointCoord-0.5;float l=length(p);if(l>0.5)discard;
        float core=smoothstep(0.5,0.0,l);gl_FragColor=vec4(uColor,core*vTw);}`,
  });
  const stars=new THREE.Points(geo,mat);
  stars.layers.set(LAYERS.ENTIRE_SCENE);
  stars.frustumCulled=false;
  scene.add(stars);
  window._starsMat=mat;
})();

(function buildMotes(){
  const N=CONFIG.atmoCount;
  const pos=new Float32Array(N*3),sizes=new Float32Array(N),seeds=new Float32Array(N);
  for(let i=0;i<N;i++){
    pos[i*3]=(Math.random()*2-1);
    pos[i*3+1]=(Math.random()*2-1);
    pos[i*3+2]=(Math.random()*2-1);
    sizes[i]=CONFIG.atmoSize*(0.4+Math.random());
    seeds[i]=Math.random()*100;
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('size',new THREE.BufferAttribute(sizes,1));
  geo.setAttribute('seed',new THREE.BufferAttribute(seeds,1));
  const mat=new THREE.ShaderMaterial({
    blending:THREE.AdditiveBlending,depthWrite:false,depthTest:false,transparent:true,
    uniforms:{uTime:{value:0},uRes:{value:new THREE.Vector2(W,H)},uColor:{value:hexToVec3(CONFIG.atmoColor)}},
    vertexShader:`attribute float size;attribute float seed;uniform float uTime;uniform vec2 uRes;varying float vA;
      vec3 warp(vec3 p,float t){float c=0.9,a=1.9,b=0.02,s=0.05;p*=2.;
        p.x+=c*sin(s*t+a*p.y)+t*b;p.y+=c*cos(s*t+a*p.x);p.y+=c*sin(s*t+a*p.z)+t*b;
        p.z+=c*cos(s*t+a*p.y);p.z+=c*sin(s*t+a*p.x)+t*b;p.x+=c*cos(s*t+a*p.z);
        return cos(p+vec3(1,2,4));}
      void main(){vec3 v=position*4.0+warp(position,uTime)*1.2;vec4 mv=modelViewMatrix*vec4(v,1.0);
        float r=length(v);float farF=1.0-smoothstep(5.0,6.5,r);float nearF=smoothstep(0.0,0.5,-mv.z);
        vA=farF*nearF;gl_PointSize=size*uRes.y/900.0/max(-mv.z,0.001);gl_PointSize=max(gl_PointSize,1.0);gl_Position=projectionMatrix*mv;}`,
    fragmentShader:`uniform vec3 uColor;varying float vA;
      void main(){vec2 p=gl_PointCoord-0.5;float l=length(p);if(l>0.5)discard;
        float tex=smoothstep(0.5,0.0,l);gl_FragColor=vec4(uColor*tex,tex*vA*0.55);}`,
  });
  const motes=new THREE.Points(geo,mat);
  motes.layers.set(LAYERS.ENTIRE_SCENE);
  motes.frustumCulled=false;
  motes.onBeforeRender=()=>{
    const t=performance.now()/1000;
    mat.uniforms.uTime.value=t*CONFIG.atmoSpeed*8;
    finalPass.uniforms.iTime.value=t;
    motes.position.copy(camera.position);
    if(window._starsMat)window._starsMat.uniforms.uTime.value=starTime;
  };
  scene.add(motes);
  window._motesMat=mat;
})();

const ENTRY_DUR=1.9, ENTRY_START_Y=-6.5;
let entryT=0, entryActive=false;
function startEntrance(){ if(!PRM){ entryActive=true; entryT=0; } }
function entryOffset(dt){
  if(!entryActive) return 0;
  entryT+=dt;
  const t=clampV(entryT/ENTRY_DUR,0,1);
  const e=1-Math.pow(1-t,3);
  const y=Lerp(ENTRY_START_Y,0,e);
  if(t>=1) entryActive=false;
  return y;
}

let curP=0, pTarget=0, curX=STOPS_X[0].v, curY=STOPS_Y[0].v, curS=STOPS_S[0].v, spinPhase=0;

if(!PRM){
  const lenis=new Lenis({duration:1.15,smoothWheel:true,touchMultiplier:1.5});
  (function rl(t){lenis.raf(t);requestAnimationFrame(rl);})(0);
}

const reveals=document.querySelectorAll('[data-reveal]');
if(PRM){ reveals.forEach(el=>el.classList.add('in')); }
else{
  const obs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');obs.unobserve(e.target);}});
  },{threshold:0.18,rootMargin:'0px 0px -8% 0px'});
  reveals.forEach(el=>obs.observe(el));
}

let last=0;
function animate(now){
  requestAnimationFrame(animate);
  const dt=clampV((now-last)/1000,0,0.05);
  last=now;

  const sh=document.body.scrollHeight, ih=window.innerHeight;
  pTarget=clampV(window.scrollY/(sh-ih)||0,0,1);
  curP+=(pTarget-curP)*Math.min(1,dt*4.5);

  const sideScale=clampV(window.innerWidth/1200,0.5,1);
  const tx=sample(STOPS_X,curP)*sideScale;
  const ty=sample(STOPS_Y,curP);
  const ts=sample(STOPS_S,curP);
  const k=Math.min(1,dt*3.2);
  curX=Lerp(curX,tx,k);
  curY=Lerp(curY,ty,k);
  curS=Lerp(curS,ts,k);

  const ey=entryOffset(dt);
  worldGroup.position.set(curX, curY+ey, 0);
  worldGroup.scale.setScalar(curS);

  spinPhase+=dt*CONFIG.spin;
  planetGroup.children.forEach(m=>{
    if(m.isMesh) m.rotation.y=CONFIG.initRotation+spinPhase+curP*Math.PI*1.6;
  });

  planetTime+=dt/12; cloudTime+=dt/20; starTime+=dt; markerTime+=dt;

  planetGroup.children.forEach(m=>{
    if(m.isMesh&&m.material&&m.material._shaderRef)
      m.material._shaderRef.uniforms.time.value=planetTime;
  });
  cloudGroup.children.forEach(cm=>{
    cm.rotation.y+=dt*cm.material._cloudSpin;
    if(cm.material._cloudShaderRef)cm.material._cloudShaderRef.uniforms.uTime.value=cloudTime;
  });
  if(window._markerMat){
    window._markerMat.uniforms.uTime.value=markerTime;
    window._markerMat.uniforms.uRes.value.set(W,H);
  }

  glowMesh.quaternion.copy(camera.quaternion);
  controls.update();

  camera.layers.set(LAYERS.TORUS_SCENE); torusComposer.render();
  finalPass.uniforms.torusTexture.value=torusComposer.renderTarget1.texture;
  camera.layers.set(LAYERS.BLOOM_SCENE); bloomComposer.render();
  finalPass.uniforms.bloomTexture.value=bloomComposer.renderTarget1.texture;
  camera.layers.set(LAYERS.ENTIRE_SCENE); finalComposer.render();
}
requestAnimationFrame(animate);

window.addEventListener('resize',()=>{
  W=window.innerWidth; H=window.innerHeight;
  camera.aspect=W/H; camera.updateProjectionMatrix();
  renderer.setSize(W,H);
  [torusComposer,bloomComposer,finalComposer].forEach(c=>{c.setSize(W,H);c.setPixelRatio(devicePixelRatio);});
  if(window._motesMat)window._motesMat.uniforms.uRes.value.set(W,H);
  if(window._starsMat)window._starsMat.uniforms.uRes.value.set(W,H);
  if(window._markerMat)window._markerMat.uniforms.uRes.value.set(W,H);
});

</script>
<script>
// Nav scroll effect
const nav=document.getElementById("mainNav");
window.addEventListener("scroll",()=>{nav.classList.toggle("scrolled",window.scrollY>60);});
// Reveal observer
const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");obs.unobserve(e.target);}});},{threshold:0.15,rootMargin:"0px 0px -6% 0px"});
document.querySelectorAll("[data-reveal],[data-rl],[data-rr]").forEach(el=>obs.observe(el));
