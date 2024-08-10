"use client"

import effectClick from "@/utils/effectClick";

export default function Bruh() {
    return(
        <div onClick={effectClick} className="flex justify-center bg-yellow-500 w-80 h-80 rounded-3xl shadow-2xl border-8 border-white m-8 p-2">
            <p className="text-5xl font-bold">Bruh</p>
        </div>
    );
}