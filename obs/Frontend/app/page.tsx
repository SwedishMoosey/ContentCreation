import Effect from "@/components/effect";
import effectPayload from "@/utils/effectInterface";

export default function Home() {
  const bruhData: effectPayload = {
    name: "Bruh",
    type: "image"
  }
  const cryingData: effectPayload = {
    name: "Crying",
    type: "video"
  }
  const rageData: effectPayload = {
    name: "Rage",
    type: "video"
  }
  const borgirData: effectPayload = {
    name: "Borgir",
    type: "video"
  }
  
  return (
    <main className="flex flex-1">
      <Effect title="Bruh" requestData={bruhData}/>
      <Effect title="Crying" requestData={cryingData}/>
      <Effect title="Rage" requestData={rageData}/>
      <Effect title="Borgir" requestData={borgirData}/>
    </main>
  );
}
