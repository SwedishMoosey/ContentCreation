import Effect from "@/components/effect";

export default function Home() {
  return (
    <main className="flex flex-1">
      <Effect title="Bruh" route="bruh"/>
      <Effect title="Crying" route="crying"/>
      <Effect title="Rage" route="rage"/>
    </main>
  );
}
