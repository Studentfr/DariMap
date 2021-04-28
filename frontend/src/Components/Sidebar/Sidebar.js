import React from 'react'
import Drawer from "./Drawer";
import SidebarContent from "./SidebarContent";

function Sidebar({id, isHidden}) {
    return(
        <div className="overflow-hidden h-screen sticky top-0 flex">
            <div className="absolute flex top-0 h-screen">
                <Drawer/>
                <SidebarContent/>
            </div>
        </div>
    )
}

export default Sidebar;